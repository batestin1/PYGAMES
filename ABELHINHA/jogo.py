
from objeto import Obj, Abelha, Texto
import random

class Jogo:
    def __init__(self):

        self.bg = Obj("assets/assets/bg.png", 0, 0)
        self.bg2 = Obj("assets/assets/bg.png", 0, -640)
        self.aranha = Obj("assets/assets/aranha1.png", random.randrange(0, 290), -50)
        self.flor = Obj("assets/assets/flor1.png",random.randrange(0, 290), -50)
        self.abelha = Abelha('assets/assets/abelha1.png', 150, 500)
        self.change_scene = False
        self.score = Texto(60, "0")
        self.vidas = Texto(60, "5")

    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.aranha.drawing(window)
        self.flor.drawing(window)
        self.abelha.drawing(window)
        self.score.draw(window, 260, 50)
        self.vidas.draw(window, 50, 50)



    def move_bg(self):
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4

        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640


    def update(self):
        self.move_bg()
        self.aranha.animacao("aranha", 8, 5)
        self.flor.animacao("flor",8, 3)
        self.mov_aranha()
        self.mov_flor()
        self.abelha.animacao("abelha", 2, 5)
        self.abelha.colisao(self.aranha.group, "aranha")
        self.abelha.colisao(self.flor.group, 'flor')
        self.game_over()
        self.vitoria()
        self.score.atualiza_texto(str(self.abelha.pontos))
        self.vidas.atualiza_texto(str(self.abelha.life))



    def mov_aranha(self):
        self.aranha.sprite.rect[1] += 10

        if self.aranha.sprite.rect[1] >= 700:
            self.aranha.sprite.kill()
            self.aranha = Obj("assets/assets/aranha1.png", random.randrange(0, 299), -50)


    def mov_flor(self):
        self.flor.sprite.rect[1] += 2

        if self.flor.sprite.rect[1] >= 700:
            self.flor.sprite.kill()
            self.flor = Obj("assets/assets/flor1.png", random.randrange(0, 299), -50)

    def game_over(self):
        if self.abelha.life <= 0:
            self.change_scene = True

    def vitoria(self):
        if self.abelha.life == 1:
            self.change_scene = True








