import pygame

class Beaker:
    def __init__(self, x, y, width=100, height=65):
        self.rect = pygame.Rect(x, y, width, height)
        self.volume = 0
        self.contents_vol = {}
        self.contents_mole = {}
        self.max_volume = 100
        self.color = (173, 216, 230)  # 初始淺藍
        
    def add_chemical(self, name, amount=0.1):
        self.volume += amount
        if self.volume > self.max_volume:
            self.volume = self.max_volume
            return
        if name in self.contents_vol:
            self.contents_vol[name] +=amount
            self.contents_mole[name] +=0.0001*amount
        else:
            self.contents_vol[name] = amount
            self.contents_mole[name] =0.0001*amount

    def update_color(self,pH,indicator_text):
        indicators = {"Methyl Orange":[3.1,"red",4.4,"yellow","orange"],
                      "Phenolphthalein":[8.2,"white",10,"purple","pink"],
                      "Bromothymol Blue":[6.0,"yellow",7.6,"blue","cyan"],
                      "Methyl Red":[4.4,"red",6.2,"yellow","orange"],
                      "Phenol Red":[6.4,"yellow",8.2,"red","orange"]
        }
        colors = {
            "red":(255,0,0),
            "yellow":(255,255,0),
            "light_yellow":(255,255,153),
            "orange":(255,165,0),
            "white":(200,200,255),
            "purple":(128,0,128),
            "green":(0,255,0),
            "cyan":(0,255,255),
            "pink":(255,105,180),
            "blue":(0,0,255),
        }
        if indicator_text == "Thymol Blue":
            if pH>9.6:
                self.color = colors["blue"]
            elif pH <1.2:
                self.color = colors["yellow"]
            elif 1.2<pH and pH<8.0:
                self.color = colors["light_yellow"]
            else:
                self.color = colors["cyan"]
        else:
            indicator = indicators[indicator_text]
            if pH<  indicator[0]:
                self.color = colors[indicator[1]]
            elif pH>indicator[2]:
                self.color = colors[indicator[3]]
            else:
                self.color = colors[indicator[4]]

    def draw(self, screen, beaker_img):
        r,g,b = self.color
        self.color2 = (min(250,r+40),min(250,g+40),min(250,b+40))
        liquid_height = int((self.volume / self.max_volume) * self.rect.height)
        liquid_rect = pygame.Rect(
            self.rect.x + 25,
            self.rect.y+ 83-liquid_height,
            self.rect.width - 50,
            liquid_height
        )
        liquid_rect2 = pygame.Rect(
            self.rect.x + 25,
            self.rect.y+ 83-liquid_height,
            self.rect.width-90,
            liquid_height
        )
        pygame.draw.rect(screen, self.color, liquid_rect)
        pygame.draw.rect(screen, self.color2, liquid_rect2)
        screen.blit(beaker_img, self.rect.topleft)