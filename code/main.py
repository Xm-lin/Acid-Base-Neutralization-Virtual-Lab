import pygame, math
from data import chemicals
from beaker import Beaker
from ui import Button
from option import data
import subprocess,os,sys

# pH更新函數
import math

def pH_update(acid_text, base_text, total_H, total_OH, vol):
    # 如果體積為 0，直接回傳中性或避免除以零錯誤
    if vol <= 0:
        return 7.0

    kb = 1.8e-5
    ka = 1.75e-5
    pKa = -math.log10(ka)
    pKb = -math.log10(kb)
    kw = 1e-14
    pH = 7.0

    # 1. 強酸 (HCl) + 強鹼 (NaOH)
    if acid_text == "HCl" and base_text == "NaOH":
        if total_H > total_OH:
            pH = -math.log10((total_H - total_OH) / vol)
        elif total_OH > total_H:
            pH = 14 + math.log10((total_OH - total_H) / vol)
        else:
            pH = 7.0

    # 2. 強酸 (HCl) + 弱鹼 (NH4OH)
    elif acid_text == "HCl" and base_text == "NH4OH":
        if total_H > total_OH: # 強酸過量
            pH = -math.log10((total_H - total_OH) / vol)
        elif total_OH > total_H: # 弱鹼緩衝區
            if total_H == 0: # 純弱鹼
                pH = 14 + math.log10(math.sqrt(kb * (total_OH / vol)))
            else: # 緩衝公式：pOH = pKb + log(共軛酸/剩餘鹼)
                pOH = pKb + math.log10(total_H / (total_OH - total_H))
                pH = 14 - pOH
        else: # 當量點：弱酸性鹽 (NH4Cl) 水解
            conc_salt = total_H / vol
            pH = 0.5 * (14 - pKb - math.log10(conc_salt))

    # 3. 弱酸 (CH3COOH) + 強鹼 (NaOH)
    elif acid_text == "CH3COOH" and base_text == "NaOH":
        if total_H > total_OH: # 弱酸緩衝區
            if total_OH == 0: # 純弱酸
                pH = -math.log10(math.sqrt(ka * (total_H / vol)))
            else: # 緩衝公式：pH = pKa + log(共軛鹼/剩餘酸)
                pH = pKa + math.log10(total_OH / (total_H - total_OH))
        elif total_OH > total_H: # 強鹼過量
            pH = 14 + math.log10((total_OH - total_H) / vol)
        else: # 當量點：弱鹼性鹽 (CH3COONa) 水解
            conc_salt = total_H / vol
            pH = 0.5 * (14 + pKa + math.log10(conc_salt))

    # 4. 弱酸 (CH3COOH) + 弱鹼 (NH4OH)
    elif acid_text == "CH3COOH" and base_text == "NH4OH":
        if total_H > total_OH: # 弱酸過量（在此簡化為緩衝計算）
            if total_OH == 0:
                pH = -math.log10(math.sqrt(ka * (total_H / vol)))
            else:
                pH = pKa + math.log10(total_OH / (total_H - total_OH))
        elif total_OH > total_H: # 弱鹼過量
            if total_H == 0:
                pH = 14 + math.log10(math.sqrt(kb * (total_OH / vol)))
            else:
                pOH = pKb + math.log10(total_H / (total_OH - total_H))
                pH = 14 - pOH
        else: # 當量點：弱酸弱鹼鹽水解
            pH = 7 + 0.5 * (pKa - pKb)

    # 邊界處理
    if pH < 0: pH = 0
    if pH > 14: pH = 14

    return round(pH, 2)

# 畫面更新函數
def update_system():
    global pH, vol
    total_H = sum(beaker.contents_mole.get(n, 0) * chemicals[n]['H+'] for n in chemicals)
    total_OH = sum(beaker.contents_mole.get(n, 0) * chemicals[n]['OH-'] for n in chemicals)
    vol = beaker.volume
    pH = pH_update(acid_text, base_text, total_H, total_OH, vol)

pygame.init()
acids = ["HCl", "CH3COOH"]
bases = ["NH4OH", "NaOH"]
indicators = ["Methyl Orange", "Phenolphthalein", "Bromothymol Blue", "Methyl Red", "Thymol Blue", "Phenol Red"]
modes = ["Titration Acid", "Titration base"]
acid_num, base_num, indicator_num, mode_num, add_vol = data()
acid_text = acids[acid_num]
base_text = bases[base_num]
mode_text = modes[mode_num]
indicator_text = indicators[indicator_num]
add_times = add_vol / 0.1

if mode_num == 0:
    use_chem = acid_text
else:
    use_chem = base_text

## 畫面設定
WIDTH, HEIGHT = 650, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("酸鹼滴定虛擬實驗室")

## 載入圖片
beaker_img = pygame.image.load("images/beaker.png").convert_alpha()
burette_img = pygame.image.load("images/burette.png").convert_alpha()

## 物件建立
mechine_x = 80
mechine_y = 540
beaker = Beaker(mechine_x, mechine_y - 100)

if mode_num == 0:
    use_btn = Button(f"drop {acid_text}", 50, 175, (210, 80, 80), "rect", "left", 150, border=10)
else:
    use_btn = Button(f"drop {base_text}", 50, 175, (70, 120, 200), "rect", "left", 150, border=10)

Auto_btn = Button("Start", 170, 240, (90, 150, 120), "rect", width=60, border=10)
speed_left = Button("speed_left", 90, 250, (110, 130, 150), "triangle")
speed_right = Button("speed_right", 140, 250, (110, 130, 150), "triangle", "right")
reset_btn = Button("Reset", 170, 462, (140, 110, 80), width=60, border=10)
Quit_btn = Button("<Back to menu", 10, 50, (90, 110, 140), "rect", width=150, border=10)
Exit_btn = Button("<Exit", 10, 10, (160,160,160), "rect", width=90, height=35, border=10)
Manual_btn = Button("Manual", 550, 600, (160,160,160), "rect", width=90, height=40, border=50)



## 參數設定
font = pygame.font.SysFont("Arial", 18, bold=True)
font_small = pygame.font.SysFont("Arial", 14, bold=True)
font_mid = pygame.font.SysFont(None, 24)
font_big = pygame.font.SysFont("Arial", 49)
clock = pygame.time.Clock()
pH = 7.0
vol = 0
drop_y = mechine_y - 150
drop_pos = [burette_img.get_width() // 2 + mechine_x, drop_y]
drop_active = False
current_chemical = None
drop_speed = 30
auto_drop = False
last_auto_drop_time = 0
drop_interval = 12.5

# pH 曲線變數
ph_history = []
point_color = []
mole_history = []
graph_rect = pygame.Rect(300, 290, 320, 240)

def defult():
    global oripH, ph_history, add_times, auto_drop, drop_interval

    while add_times > 0:
        if mode_text == "Titration Acid":
            current_chemical = base_text
        else:
            current_chemical = acid_text

        beaker.add_chemical(current_chemical)
        update_system()

        if add_times == 1:
            oripH = pH
            ph_history.append(pH)
            beaker.update_color(pH, indicator_text)
            point_color.append(beaker.color)
            mole_history.append((beaker.contents_mole.get(acid_text, 0), beaker.contents_mole.get(base_text, 0)))
            break

        add_times -= 1
        auto_drop = False

defult()

# ── 顏色定義 ──────────────────────────────────────────────
BG_MAIN = (255,240,220)
BG_PANEL = (220, 232, 242)
BG_PANEL_IN = (235, 243, 250)
CARD_HEADER = (190, 210, 228)
CARD_BORDER = (130, 155, 180)
GRAPH_BG = (248, 248, 244)
GRID_LINE = (210, 210, 205)
TEXT_DARK = (35, 45, 55)
TEXT_MID = (80, 95, 110)
ACCENT_TEAL = (38, 145, 135)
# ─────────────────────────────────────────────────────────

running = True
while running:
    # ── 背景 ──────────────────────────────────────────────
    screen.fill(BG_MAIN)

    # 左側面板（底色 + 白內框）
    pygame.draw.rect(screen, BG_PANEL, (0, 0, 250, 670))
    pygame.draw.rect(screen, BG_PANEL_IN, (3, 3, 244, 670))

    for btn in [use_btn, reset_btn, Quit_btn, Auto_btn, speed_right, speed_left,Manual_btn,Exit_btn]:
        btn.update()
        btn.draw(screen, font)

    screen.blit(font.render(f"Indicator :", True, TEXT_DARK), (25, 585))
    pygame.draw.line(screen, (190, 205, 220), (90, 623), (230, 623), 2)
    screen.blit(font.render(f"{indicators[indicator_num]}", True, ACCENT_TEAL), (93, 605))
    screen.blit(font.render(f"Manual Titration:", True, TEXT_MID), (10, 150))
    screen.blit(font.render(f"Auto Titration:", True, TEXT_MID), (10, 220))
    screen.blit(font.render(f"speed:", True, TEXT_MID), (10, 250))
    screen.blit(font.render(f"{1000 // drop_interval:>2.0f}D/s", True, TEXT_DARK), (93, 250))

    ## pH曲線圖
    screen.blit(font.render("pH Curve:", True, TEXT_MID), (graph_rect.x - 40, graph_rect.y - 50))
    screen.blit(pygame.transform.rotate(font.render("pH", True, TEXT_MID), 90), (graph_rect.x - 45, graph_rect.y + 110))

    xlabel = f"drop{use_chem:^7}vol(ml)" if acid_num == 0 else f"drop{use_chem:^9}vol(ml)"
    screen.blit(font.render(xlabel, True, TEXT_MID), (graph_rect.x + 105, graph_rect.bottom + 30))

    pygame.draw.rect(screen, GRAPH_BG, graph_rect)
    screen.blit(font.render(f"{str(0):^3}", True, TEXT_DARK), (graph_rect.left - 18, graph_rect.bottom))

    for i in range(0, 21):
        if (i % 5 == 0) and i != 0:
            screen.blit(font.render(f"{str(i * 5):^3}", True, TEXT_DARK), (graph_rect.left + graph_rect.width * i / 20 - 8, graph_rect.bottom + 2))

        pygame.draw.line(
            screen,
            GRID_LINE,
            (graph_rect.left + graph_rect.width * i / 20, graph_rect.top),
            (graph_rect.left + graph_rect.width * i / 20, graph_rect.bottom),
            1
        )

    for i in range(-1, 15):
        if i == -1 or i == 6:
            screen.blit(font.render(f"{str(14 - i - 1):^3}", True, TEXT_DARK), (graph_rect.left - 17, graph_rect.top + graph_rect.height * i / 14 + 7))

        if i != -1:
            pygame.draw.line(
                screen,
                GRID_LINE,
                (graph_rect.left, graph_rect.top + graph_rect.height * i / 14),
                (graph_rect.right, graph_rect.top + graph_rect.height * i / 14),
                1
            )

    pygame.draw.rect(screen, CARD_BORDER, graph_rect, 1)
    pygame.draw.line(screen, (180, 195, 195), (graph_rect.left, graph_rect.centery), (graph_rect.right, graph_rect.centery), 1)

    # 繪製點與線，並偵測當量點
    points = []
    display_history = ph_history[-40:]
    display_moles = mole_history[-40:]

    for i, val in enumerate(display_history):
        x = graph_rect.left + 2 * (i * (graph_rect.width / 40))
        y = graph_rect.bottom - (val * (graph_rect.height / 14))
        points.append((x, y))

    if len(points) > 1:
        pygame.draw.lines(screen, TEXT_DARK, False, points, 2)

    for i, val in enumerate(display_history):
        px, py = points[i]
        pygame.draw.circle(screen, point_color[i], (int(px), int(py)), 4)
        pygame.draw.circle(screen, TEXT_DARK, (int(px), int(py)), 4, 2)

        # 當量點偵測與繪製
        acid_m, base_m = display_moles[i]

        if abs(acid_m - base_m) < 1e-9 and acid_m > 0:
            box_w, box_h = 85, 30

            if mode_num == 0:
                bx, by = px+20, py - 50
                pygame.draw.rect(screen, (248, 248, 245), (bx, by, box_w, box_h), border_radius=15)
                pygame.draw.rect(screen, CARD_BORDER, (bx, by, box_w, box_h), 1, border_radius=15)
                pygame.draw.circle(screen, TEXT_DARK, (int(px), int(py)), 6, 2)
                pygame.draw.line(screen, TEXT_DARK, (px, py), (bx, by+box_h//2), 2)
                label = font_small.render("Equivalence", True, TEXT_DARK)
                screen.blit(label, (bx + 10, by + 6))

            else:
                bx, by = px+20, py + 50
                pygame.draw.rect(screen, (248, 248, 245), (bx, by, box_w, box_h), border_radius=15)
                pygame.draw.rect(screen, CARD_BORDER, (bx, by, box_w, box_h), 1, border_radius=15)
                pygame.draw.circle(screen, TEXT_DARK, (int(px), int(py)), 6, 2)
                pygame.draw.line(screen, TEXT_DARK, (px+2, py), (bx, by+box_h//2), 2)
                label = font_small.render("Equivalence", True, TEXT_DARK)
                screen.blit(label, (bx+10, by+6))

    ### 右側數值區
    x_offset, y_offset = 270, 70
    pygame.draw.rect(screen, (245, 248, 252), (x_offset - 10, y_offset - 50, 180, 150), border_radius=15)
    pygame.draw.rect(screen, CARD_HEADER, (x_offset - 10, y_offset - 50, 180, 40), border_top_left_radius=15, border_top_right_radius=15)
    pygame.draw.rect(screen, CARD_BORDER, (x_offset - 10, y_offset - 50, 180, 150), width=4, border_radius=15)
    screen.blit(font.render("Titration Data", True, TEXT_DARK), (x_offset + 30, y_offset - 37))
    screen.blit(font.render(acid_text, True, TEXT_DARK), (x_offset + 10, y_offset))
    screen.blit(font.render(f"{beaker.contents_vol.get(acid_text, 0):<4.1f}", True, TEXT_DARK), (x_offset + 84, y_offset))
    screen.blit(font.render("mL", True, TEXT_DARK), (x_offset + 120, y_offset))

    y_offset += 30
    screen.blit(font.render(base_text, True, TEXT_DARK), (x_offset + 10, y_offset))
    screen.blit(font.render(f"{beaker.contents_vol.get(base_text, 0):<4.1f}", True, TEXT_DARK), (x_offset + 84, y_offset))
    screen.blit(font.render("mL", True, TEXT_DARK), (x_offset + 120, y_offset))

    y_offset += 30
    pygame.draw.rect(screen, CARD_BORDER, (x_offset, y_offset, 160, 4), border_radius=10)

    y_offset += 10
    screen.blit(font.render(f"Total", True, TEXT_DARK), (x_offset + 10, y_offset))
    screen.blit(font.render(f"{beaker.volume:.1f}", True, TEXT_DARK), (x_offset + 84, y_offset))
    screen.blit(font.render("mL", True, TEXT_DARK), (x_offset + 120, y_offset))

    # pH數據顯示
    pygame.draw.rect(screen, (245, 248, 252), (460, 20, 180, 150), border_radius=15)
    pygame.draw.rect(screen, CARD_HEADER, (460, 20, 180, 40), border_top_left_radius=15, border_top_right_radius=15)
    pygame.draw.rect(screen, CARD_BORDER, (460, 20, 180, 150), width=4, border_radius=15)
    screen.blit(font.render("      pH Data", True, TEXT_DARK), (495, 33))

    x_st, y_st = 480, 140
    pygame.draw.line(screen, TEXT_DARK, (x_st, y_st), (x_st + 130, y_st), 2)

    for i in range(15):
        if i == 0 or i == 7 or i == 14:
            pygame.draw.line(screen, TEXT_DARK, (480 + i * (130/14), y_st), (480 + i * (130/14), y_st - 10), 2)
            screen.blit(font.render(str(i), True, TEXT_DARK), (480 + i * (130/14) - 4, y_st + 4))
        else:
            pygame.draw.line(screen, TEXT_MID, (480 + i * (130/14), y_st), (480 + i * (130/14), y_st - 5), 2)

    screen.blit(font.render(f"pH={pH:.2f}", True, TEXT_DARK), (480, y_st - 75))
    screen.blit(font_big.render("ˇ", True, TEXT_DARK), (480 - 1 + (130 * (pH / 14)), (y_st - 35)))

    ### 反應區動畫
    screen.blit(burette_img, (mechine_x - 3, mechine_y - 250))
    beaker.draw(screen, beaker_img)

    if beaker.volume >= beaker.max_volume or beaker.volume >= add_vol*3:
        screen.blit(font.render("Titration Compelete!", True, (200, 60, 60)), (mechine_x-20, mechine_y - 130))
        auto_drop = False

    if beaker.volume-add_vol > add_vol-0.5 and beaker.volume-add_vol < add_vol+0.5:
        drop_interval = 250

    if drop_active:
        drop_color = (210, 70, 70) if current_chemical in ["HCl", "CH3COOH"] else (60, 100, 200)
        pygame.draw.circle(screen, drop_color, (int(drop_pos[0]), int(drop_pos[1])), 5)
        drop_pos[1] += drop_speed

        if drop_pos[1] >= 480:
            beaker.add_chemical(current_chemical)
            update_system()

            if round(beaker.contents_vol.get(acid_text if mode_num==0 else base_text, 0), 3) % 2.5 == 0:
                ph_history.append(pH)
                point_color.append(beaker.color)
                mole_history.append((
                    beaker.contents_mole.get(acid_text if mode_num==0 else base_text, 0),
                    beaker.contents_mole.get(base_text if mode_num==0 else acid_text, 0)
                ))

            drop_pos[1] = drop_y
            drop_active = False

    current_time = pygame.time.get_ticks()

    if auto_drop and not drop_active and beaker.volume < beaker.max_volume:
        if current_time - last_auto_drop_time >= drop_interval:
            current_chemical = acid_text if mode_num == 0 else base_text
            drop_active = True
            beaker.update_color(pH, indicators[indicator_num])
            last_auto_drop_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            for b in [use_btn, reset_btn, Quit_btn, Auto_btn, speed_right, speed_left,Manual_btn,Exit_btn] :
                b.touched = b.rect.collidepoint(pos)

        if use_btn.is_clicked(event):
            if beaker.volume < beaker.max_volume:
                current_chemical = acid_text if mode_num == 0 else base_text
                drop_active = True
                beaker.update_color(pH, indicators[indicator_num])

        if speed_right.is_clicked(event):
            drop_interval = max(12.5, drop_interval // 2)

        if speed_left.is_clicked(event):
            drop_interval = min(1000, drop_interval * 2)

        if Auto_btn.is_clicked(event):
            auto_drop = not auto_drop
            Auto_btn.text = "Stop" if auto_drop else "Start"
            Auto_btn.color = (200, 60, 60) if auto_drop else (90, 150, 120)

            if auto_drop:
                last_auto_drop_time = pygame.time.get_ticks()

        if Exit_btn.is_clicked(event):
            running = False

        if reset_btn.is_clicked(event):
            beaker = Beaker(mechine_x, mechine_y - 100)
            beaker.color = (173, 216, 230)
            pH = oripH
            ph_history = []
            mole_history = []
            point_color = []
            auto_drop = False
            drop_interval = 1000
            add_times = add_vol / 0.1
            defult()

        if Manual_btn.is_clicked(event):
            os.startfile("manual\manual.txt") 

        if Quit_btn.is_clicked(event):
            subprocess.Popen([sys.executable, "main.py"])
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()