import pygame


class Objeto(pygame.sprite.Sprite):
    def __init__(self, img, x, y, *groups):
        super().__init__ (*groups)

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y



class Alien(Objeto):
    def __init__(self, img, x, y, *groups) :
        super().__init__(img, x, y, *groups)

    def update(self):
        self.mov()

    def mov(self):
        self.rect[0] -= 4
        if self.rect[0] <= -100:
            self.kill()

class Moeda(Objeto):
    def __init__(self, img, x, y, *groups) :
        super().__init__(img, x, y, *groups)

        self.tempo =0

    def update(self, *args):
        self.mov()
        self.animacao()

    def mov(self):
        self.rect[0] -= 4
        if self.rect[0]<=-100 :
            self.kill()

    def animacao(self):
        self.tempo = (self.tempo + 1) % 6
        self.image = pygame.image.load("assets/" + str(self.tempo) + ".png")



class Astrounauta(Objeto):
    def __init__(self, img, x, y, *groups) :
        super().__init__(img, x, y, *groups)

        self.tick = 0
        self.velocidade = 5
        self.grav = 1
        self.jogo = True
        self.pontuacao = 0

    def update(self, *args):
        self.mov()

        self.animacao()

    def mov(self):
        key = pygame.key.get_pressed()

        self.velocidade += self.grav
        self.rect[1] += self.velocidade

        if self.velocidade >= 15:
            self.vel = 15

        if self.jogo:
            if key[pygame.K_UP]:
                self.velocidade -= 5


        if self.rect[1] >= 440:
            self.rect[1] = 440
        elif self.rect[1] <= 0:
            self.rect[1]=0
            self.velocidade = 4





    def animacao(self):
        self.tick = (self.tick + 1) % 4
        self.image = pygame.image.load("assets/astro" + str(self.tick) + ".png")




    def colisao_Alien(self, group):

        colide = pygame.sprite.spritecollide(self, group, False)
        if colide:
            self.jogo = False

    def colisao_Moeda(self,group):

        colide = pygame.sprite.spritecollide(self,group, True)
        if colide:
            self.pontuacao += 1



class Texto(Objeto):
    pygame.init()
    def __init__(self, size, texto):
        self.font = pygame.font.Font("assets/font/sonic_advance_2.ttf", size)
        self.render = self.font.render(texto, True, (255, 255, 255))

    def desenho(self, janela, x, y):
       janela.blit(self.render, (x, y))

    def texto_update(self, texto):
        self.render = self.font.render(texto, True, (255, 255, 255))


class Satelite(Objeto):
    def __init__(self, img, x, y, *groups) :
        super().__init__(img, x, y, *groups)
        self.tempo = -1

    def update(self):
        self.move()

    def move(self) :
        self.rect[-1] -= 4
        if self.rect[-1]<=-50 :
            self.rect[-1] = -100


    def animacao(self) :
        self.tempo = (self.tempo + 0) % 3
        self.image = pygame.image.load("assets/sate" + str(self.tempo) + ".png")













