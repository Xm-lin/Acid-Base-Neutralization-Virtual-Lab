import pygame

class Button:
    def __init__(self, text, x, y, color, shape="rect", side="left", width=100, height=35, border=5):
        self.shape = shape
        self.text = text
        self.border = border
        self.color = color

        r, g, b = self.color
        self.pressed = False
        self.touched = False
        self.color2 = (
            min(255, r + 50),
            min(255, g + 50),
            min(255, b + 50)
        )

        if shape == "rect":
            self.rect = pygame.Rect(x, y, width, height)
            self.rect2 = pygame.Rect(x + 3, y + 3, width, height)

        elif shape == "triangle":
            self.top = (x, y)
            self.bottom = (x, y + 20)

            if side == "left":
                self.side = (x - 20, y + 10)
                self.coordinate2 = [
                    (self.top[0] - 2, self.top[1] + 4),
                    (self.bottom[0] - 2, self.bottom[1] - 4),
                    (self.side[0] + 4, self.side[1])
                ]
                self.rect2 = (self.top[0] - 22, self.top[1] - 1, 25, 25)
            else:
                self.side = (x + 20, y + 10)
                self.coordinate2 = [
                    (self.top[0] + 2, self.top[1] + 4),
                    (self.bottom[0] + 2, self.bottom[1] - 4),
                    (self.side[0] - 4, self.side[1])
                ]
                self.rect2 = (self.top[0] - 2, self.top[1] - 1, 25, 25)

            self.coordinate = [self.top, self.bottom, self.side]

            self.rect = pygame.Rect(
                min(self.top[0], self.bottom[0], self.side[0]),
                min(self.top[1], self.bottom[1], self.side[1]),
                abs(self.side[0] - self.top[0]),
                abs(self.bottom[1] - self.top[1])
            )

    #每幀更新按壓狀態
    def update(self):
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if mouse[0] and self.rect.collidepoint(pos):
            self.pressed = True
        else:
            self.pressed = False


    def draw(self, screen, font):
        if self.shape == "rect":
            #按下變暗效果
            if self.touched and self.pressed==False:
                color = (
                    max(0, self.color[0] - 30),
                    max(0, self.color[1] - 30),
                    max(0, self.color[2] - 30)
                )
            elif self.pressed:
                color = (
                    max(0, self.color[0] - 80),
                    max(0, self.color[1] - 80),
                    max(0, self.color[2] - 80)
                )
            else:
                color = self.color

            pygame.draw.rect(screen, (80, 80, 80), self.rect2, border_radius=self.border)
            pygame.draw.rect(screen, color, self.rect, border_radius=self.border)

            text_surf = font.render(self.text, True, (0, 0, 0))
            screen.blit(
                text_surf,
                (
                    self.rect.x + (self.rect.width - text_surf.get_width()) // 2,
                    self.rect.y + (self.rect.height - text_surf.get_height()) // 2
                )
            )

        elif self.shape == "triangle":
            if self.pressed:
                color_to_use = (
                    max(0, self.color[0] - 60),
                    max(0, self.color[1] - 60),
                    max(0, self.color[2] - 60)
                )
            else:
                color_to_use = self.color

            pygame.draw.polygon(screen, color_to_use, self.coordinate)
            pygame.draw.polygon(screen, self.color2, self.coordinate2)

    def click(self, pos):
        return self.rect.collidepoint(pos)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos)