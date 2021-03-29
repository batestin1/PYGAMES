import pygame
from objetos import Objeto
from jogo import Jogo
from menu import Menu

class Main:
    def __init__(self):
        self.janela = pygame.display.set_mode([360, 640]) #janela para iniciar o pygame
        self.title = pygame.display.set_caption("ASTRO SPACE") # titulo do jogo
        self.loop = True #controla o loop, sempre verdadeiro
        self.fps = pygame.time.Clock() #controla o FPS da animação
        self.jogo = Jogo()
        self.menu = Menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #controla o evento que fecha a janela do pygame
                pygame.quit()
                self.loop = False

            if not self.menu.troca_cenario:
                self.menu.events(event)

    def draw(self): #esta função importa os desenhos para o jogo

        if not self.menu.troca_cenario:
            self.menu.update(str(self.jogo.pontuacao_Final))
            self.menu.draw(self.janela)

        elif not self.jogo.troca_cenario:
            self.jogo.desenho(self.janela)
            self.jogo.update()
        else:
            self.loop = False

    def update(self): #esta função é responsavel por fazer o jogo funcionar
        while self.loop:
            self.fps.tick(30)
            self.events()
            self.draw()
            pygame.display.update()

loop = True
while loop:
    Main().update()
    pygame.init()