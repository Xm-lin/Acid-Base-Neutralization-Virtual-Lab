import sys
import pygame
import os,subprocess
from ui import Button

def point_in_triangle(pt, tri):
    (x1, y1), (x2, y2), (x3, y3) = tri

    def sign(p1, p2, p3):
        return (p1[0]-p3[0])*(p2[1]-p3[1]) - (p2[0]-p3[0])*(p1[1]-p3[1])

    b1 = sign(pt, (x1,y1), (x2,y2)) < 0.0
    b2 = sign(pt, (x2,y2), (x3,y3)) < 0.0
    b3 = sign(pt, (x3,y3), (x1,y1)) < 0.0

    return (b1 == b2) and (b2 == b3)

pygame.init()
WIDTH = 300
HEIGHT = 530
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Option")
font2 = pygame.font.SysFont(None, 23)
font = pygame.font.SysFont(None, 24)

# ── 顏色定義（與 main.py 同系）────────────────────────────
BG_MAIN = (255,240,220)
PANEL_CARD = (235, 243, 250)
CARD_HDR = (190, 210, 228)
CARD_BORDER = (130, 155, 180)
TEXT_DARK = (35, 45, 55)
TEXT_GRAY = (170, 170, 170)
TEXT_MID = (80, 95, 110)
ACCENT_RED = (200, 70, 70)
ACCENT_BLUE = (60, 100, 190)
ACCENT_PURP = (150, 80, 180)
ACCENT_GRAY = (100, 125, 145)
CONFIRM_CLR = (55, 140, 120)
WHITE_BOX = (250, 250, 248)
# ─────────────────────────────────────────────────────────

# 建立按鈕
left_x = 90
right_x = 200
Buttons = [
    Button("acid_left", left_x, 100, ACCENT_RED, "triangle"),
    Button("acid_right", right_x, 100, ACCENT_RED, "triangle", "right"),
    Button("base_left", left_x, 180, ACCENT_BLUE, "triangle"),
    Button("base_right", right_x, 180, ACCENT_BLUE, "triangle", "right"),
    Button("indicator_left", left_x-30, 260, ACCENT_PURP, "triangle"),
    Button("indicator_right", right_x+30, 260, ACCENT_PURP, "triangle", "right"),
    Button("mode_left", left_x-10, 340, ACCENT_GRAY, "triangle"),
    Button("mode_right", right_x+10, 340, ACCENT_GRAY, "triangle", "right"),
    Button("vol_left", left_x+5, 390, ACCENT_GRAY, "triangle"),
    Button("vol_right", right_x-5, 390, ACCENT_GRAY, "triangle", "right"),
    Button("Confirm", 85, 430, CONFIRM_CLR, "rect", width=120, height=40, border=50),
    Button("Manual", 200, 480, TEXT_GRAY, "rect", width=90, height=40, border=50),
]

# data
acids = ["HCl","CH3COOH"]
acid_num = 0
bases = ["NH4OH","NaOH"]
base_num = 0
indicators = ["Methyl Orange","Phenolphthalein","Bromothymol Blue","Methyl Red","Thymol Blue","Phenol Red"]
indicator_num = 0
modes = ["Titration Acid","Titration base"]
mode_num = 0
add_vol = 15

def data():
    return acid_num,base_num,indicator_num,mode_num,add_vol

# 顯示區
acid_bg = pygame.Rect(95, 90, 100, 40)
base_bg = pygame.Rect(95, 170, 100, 40)
indicator_bg = pygame.Rect(66, 250, 160, 40)
mode_bg = pygame.Rect(85, 330, 122, 40)
add_vol_bg = pygame.Rect(100, 380, 90, 40)

running = True
while running:
    screen.fill(BG_MAIN)

    # ── 頂部標題卡片 ─────────────────────────────────────
    pygame.draw.rect(screen, PANEL_CARD, (10, 16, 147, 35), border_radius=12)
    pygame.draw.rect(screen, CARD_HDR, (10, 16, 146, 35), border_radius=12)
    pygame.draw.rect(screen, CARD_BORDER, (10, 16, 147, 35), width=2, border_radius=12)
    title = font2.render("Choose Option:", True, TEXT_DARK)
    screen.blit(title, (20, 27))

    # ── 各選項白框 ────────────────────────────────────────
    for rect in [acid_bg, base_bg, indicator_bg, mode_bg, add_vol_bg]:
        pygame.draw.rect(
            screen,
            WHITE_BOX,
            rect,
            border_bottom_left_radius=80,
            border_top_left_radius=80,
            border_bottom_right_radius=100,
            border_top_right_radius=100
        )
        pygame.draw.rect(
            screen,
            CARD_BORDER,
            rect,
            width=2,
            border_bottom_left_radius=80,
            border_top_left_radius=80,
            border_bottom_right_radius=100,
            border_top_right_radius=100
        )

    # ── 標籤文字 ──────────────────────────────────────────
    screen.blit(font.render("Acid:", True, TEXT_MID), (acid_bg.x-80, acid_bg.y-25))
    screen.blit(font.render("Base:", True, TEXT_MID), (base_bg.x-80, base_bg.y-25))
    screen.blit(font.render("Indicator:", True, TEXT_MID), (indicator_bg.x-52, indicator_bg.y-25))
    screen.blit(font.render("Mode:", True, TEXT_MID), (mode_bg.x-70, mode_bg.y-25))

    # ── 選項值文字（各自配色）────────────────────────────
    screen.blit(font.render(f"{acids[acid_num]}", True, ACCENT_RED), (acid_bg.x+7, acid_bg.y+13))
    screen.blit(font.render(f"{bases[base_num]}", True, ACCENT_BLUE), (base_bg.x+7, base_bg.y+13))
    screen.blit(font.render(f"{indicators[indicator_num]}", True, ACCENT_PURP), (indicator_bg.x+7, indicator_bg.y+13))
    screen.blit(font.render(f"{modes[mode_num]}", True, ACCENT_GRAY), (mode_bg.x+7, mode_bg.y+13))
    screen.blit(font.render(f"Add {add_vol} ml", True, ACCENT_GRAY), (add_vol_bg.x+7, add_vol_bg.y+13))

    # 畫按鈕
    for b in Buttons:
        b.draw(screen, font)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            for b in Buttons:
                if b.shape == "triangle":
                    b.touched = point_in_triangle(pos, b.coordinate)
                else:
                    b.touched = b.rect.collidepoint(pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in Buttons:
                if b.is_clicked(event):
                    if b.text == "acid_left":
                        acid_num = acid_num-1
                        if acid_num == -1:
                            acid_num = 1
                        if acid_num ==1:
                            base_num=1

                    if b.text == "acid_right":
                        acid_num = acid_num+1
                        if acid_num == 2:
                            acid_num = 0
                        if acid_num ==1:
                            base_num=1

                    if acid_num == 1:
                        base_num = 1

                    if b.text == "base_left":
                        if acid_num == 1:
                            base_num = 1
                            continue
                        base_num = base_num-1
                        if base_num == -1:
                            base_num = 1
                        

                    if b.text == "base_right":
                        if acid_num == 1:
                            base_num = 1
                            continue
                        base_num = base_num+1
                        if base_num == 2:
                            base_num = 0
                        

                    if b.text == "indicator_left":
                        indicator_num -= 1
                        if indicator_num == 0:
                            indicator_num = 5

                    if b.text == "indicator_right":
                        indicator_num += 1
                        if indicator_num == 5:
                            indicator_num = 0

                    if b.text == "mode_left":
                        mode_num -= 1
                        if mode_num == 0:
                            mode_num = 1

                    if b.text == "mode_right":
                        mode_num += 1
                        if mode_num == 2:
                            mode_num = 0

                    if b.text == "Manual":
                        os.startfile("說明書.txt") 

                    if b.text == "vol_left":
                        add_vol = max(add_vol-5,15)

                    if b.text == "vol_right":
                        add_vol = min(add_vol+5,25)

                    if b.text == "Confirm":
                        running = False

    pygame.display.flip()

pygame.quit()