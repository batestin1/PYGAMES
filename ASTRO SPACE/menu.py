from objetos import Objeto, Texto
import pygame

class Menu:
    def __init__(self):
        self.todo_grupo = pygame.sprite.Group()
        self.fundo = Objeto("assets/space.png", 0, 0, self.todo_grupo)
        self.fundo2 = Objeto("assets/space.png", 360, 0, self.todo_grupo)
        self.chao = Objeto("assets/ground.png", 0, 480, self.todo_grupo)
        self.chao2 = Objeto("assets/ground.png", 360, 480, self.todo_grupo)

        self.start = Objeto("assets/getready.png", 60, 190, self.todo_grupo)
        self.tabela = Objeto("assets/score.png", 20, 250, self.todo_grupo)
        self.go = Objeto("assets/go.png", 100, 450, self.todo_grupo)

        self.troca_cenario = False
        self.texto_pontos = Texto(100,"0")

    def draw(self, janela):
        self.todo_grupo.draw(janela)
        self.texto_pontos.desenho(janela, 160, 320)

    def update(self, pontos):
        self.todo_grupo.update()
        self.mov_fundo()
        self.mov_chao()
        self.texto_pontos.texto_update(pontos)


    def events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.go.rect.collidepoint(pygame.mouse.get_pos()):
                self.troca_cenario = True
                print("mouse")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.troca_cenario = True
                print('teclado')

    def mov_fundo(self) :  # induz o movimento do fundo
        self.fundo.rect[0] -= 1
        self.fundo2.rect[0] -= 1

        if self.fundo.rect[0]<=-360 :
            self.fundo.rect[0] = 0

        if self.fundo2.rect[0]<=0 :
            self.fundo2.rect[0] = 360

    def mov_chao(self) :  # induz o movimento do chao
        self.chao.rect[0] -= 4
        self.chao2.rect[0] -= 4

        if self.chao.rect[0]<=-360 :
            self.chao.rect[0] = 0

        if self.chao2.rect[0]<=0 :
            self.chao2.rect[0] = 360
