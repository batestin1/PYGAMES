
import pygame
from objetos import Objeto, Alien, Moeda, Astrounauta, Texto, Satelite
import random

class Jogo:

    def __init__(self):
        self.todo_grupo = pygame.sprite.Group()
        self.moeda_grupo = pygame.sprite.Group()
        self.aliens_grupo = pygame.sprite.Group()


        self.fundo = Objeto("assets/space.png", 0, 0, self.todo_grupo)
        self.fundo2= Objeto("assets/space.png", 360, 0, self.todo_grupo)
        self.chao = Objeto("assets/ground.png", 0, 480, self.todo_grupo)
        self.chao2 = Objeto("assets/ground.png", 360, 480, self.todo_grupo)
        self.pontos = Texto(100, "0")
        self.astronauta = Astrounauta("assets/astro0.png", 50, 320, self.todo_grupo)
        self.tempo = 0
        self.tempo2 = 0
        self.timer = 0
        self.troca_cenario = False
        self.pontuacao_Final = 0
        self.verificandoPontuacao()


    def desenho(self, janela):
        self.todo_grupo.draw(janela)
        self.pontos.desenho(janela, 150, 50 )

    def update(self):
        #self.todo_grupo.update()
        self.mov_fundo()
        self.mov_chao()
        if self.astronauta.jogo :
            self.novos_aliens()

            self.astronauta.colisao_Alien(self.aliens_grupo)

            self.astronauta.colisao_Moeda(self.moeda_grupo)
            self.pontos.texto_update(str(self.astronauta.pontuacao))
            self.todo_grupo.update()
        else:
            self.guardandoPontos()
            self.gameover()





    def mov_fundo(self): #induz o movimento do fundo
        self.fundo.rect[0] -=1
        self.fundo2.rect[0] -=1

        if self.fundo.rect[0] <= -360:
            self.fundo.rect[0] = 0

        if self.fundo2.rect[0] <= 0:
            self.fundo2.rect[0] = 360

    def mov_chao(self) :  # induz o movimento do chao
        self.chao.rect[0] -= 4
        self.chao2.rect[0] -= 4

        if self.chao.rect[0]<=-360 :
            self.chao.rect[0] = 0

        if self.chao2.rect[0]<=0 :
            self.chao2.rect[0] = 360


    def novos_aliens(self):
        self.tempo +=1
        if self.tempo >= random.randrange(60, 110):
            self.tempo = 0
            alien = Alien("assets/alien1.png", 360, random.randrange(300, 450), self.todo_grupo, self.aliens_grupo )
            moeda = Moeda("assets/0.png", 332, alien.rect[1] - 100, self.todo_grupo, self.moeda_grupo)

    def gameover(self) :
        self.timer += 1
        if self.timer>= 10:
            self.troca_cenario = True

    def guardandoPontos(self):
        if self.astronauta.pontuacao > self.pontuacao_Final:
            self.pontuacao_Final = self.astronauta.pontuacao

            arquivo = open("pontos.txt", "w")
            arquivo.write(str(self.pontuacao_Final))
            arquivo.close()

    def verificandoPontuacao(self):

        arquivo2 = open("pontos.txt", "r")
        self.pontuacao_Final = int(arquivo2.read())
        arquivo2.close()




























