


import pygame

class Obj:

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.frame=1
        self.tick = 0

    def drawing(self, window):
        self.group.draw(window)

    def animacao(self, image, tick, frames):
        self.tick +=1

        if self.tick == tick:
            self.tick = 0
            self.frame += 1
        if self.frame == frames:
            self.frame = 1
        self.sprite.image = pygame.image.load("assets/assets/" + image + str(self.frame) + ".png")


class Abelha(Obj):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.life = 5
        self.pontos = 0


    def move_abelha(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30

    def colisao(self, group, nome):
        nome = nome
        colisao = pygame.sprite.spritecollide(self.sprite, group, True)

        if nome == "flor" and colisao:
            self.pontos +=1


        elif nome == "aranha" and colisao:
           self.life -= 1



class Texto:
    def __init__(self, size, text):
        self.font = pygame.font.SysFont("arial", size)
        self.render = self.font.render(text, True, (0,0,255))

    def draw(self, window, x, y):
        window.blit(self.render, (x,y))

    def atualiza_texto(self, atual):
        self.render = self.font.render(atual, True, (0,0,255))





