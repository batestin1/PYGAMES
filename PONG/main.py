import pygame

# declarando as variaveis

repeticao = True
background = pygame.image.load('assets/field.png')
window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption('Futebol Pong')


jogador1 = pygame.image.load('assets/player1.png')
j1_Y = 310
j1_CIMA = False
j1_BAIXO = False

textoFinal = pygame.image.load('assets/win.png')

pontos1 = 0
pontos1_img = pygame.image.load('assets/score/0.png')

pontos2= 0
pontos2_img = pygame.image.load('assets/score/0.png')

jogador2 = pygame.image.load('assets/player2.png')
j2_Y = 310
bola = pygame.image.load('assets/ball.png')
bolaX = 617
bolaY = 337
bolaDirX = -8
bolaDirY = 8

barra = pygame.image.load('assets/bar.png')



#função de movimento da bola
def bolaMovimento():
    global bolaX
    global bolaY
    global bolaDirX
    global bolaDirY
    global pontos1
    global pontos2
    global pontos2_img
    global pontos1_img

    bolaX += bolaDirX
    bolaY += bolaDirY

    if bolaX < 125:
        if j1_Y < bolaY + 23:
            if j1_Y + 146 > bolaY:
                bolaDirX *= -1
    if bolaX > 1107:
        if j2_Y < bolaY + 23:
            if j2_Y + 146 > bolaY:
                bolaDirX *= -1
    if bolaY > 690:
        bolaDirY *= -1
    elif bolaY <= 0:
        bolaDirY *= -1

    if bolaX < -50:
        bolaX = 617
        bolaY = 337
        bolaDirY *= -1
        bolaDirX *= -1
        pontos2 += 1
        pontos2_img = pygame.image.load('assets/score/' + str(pontos2) +'.png')


    elif bolaX > 1320:
        bolaX = 617
        bolaY = 337
        bolaDirY *= -1
        bolaDirX *= -1
        pontos1 += 1
        pontos1_img = pygame.image.load('assets/score/' + str(pontos1) + '.png')


#função para armazenar desenhos
def desenho():
    # criando a janela do jogo
    window.blit(background, (0, 0))

    if pontos1 or pontos2 < 3:
        window.blit(jogador1, (50, j1_Y))
        window.blit(jogador2, (1150, j2_Y))
        window.blit(bola, (bolaX, bolaY))
        window.blit(pontos1_img, (500, 50))
        window.blit(pontos2_img, (710, 50))

    else:
        window.blit(textoFinal, (300, 300))

def mov_jogador():
    global j1_Y

    if j1_CIMA:
        j1_Y -= 8
    else:
        j1_Y += 0

    if j1_BAIXO:
        j1_Y += 8
    else:
        j1_Y += 0

    if j1_Y <= 0:
        j1_Y = 0
    elif j1_Y >= 566:
        j1_Y = 566

def mov_jogador2():
    global j2_Y
    global bolaY

    j2_Y = bolaY



#iniciando o pygame
pygame.init()





while repeticao:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            repeticao = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                j1_CIMA = True
            if e.key == pygame.K_DOWN:
                j1_BAIXO = True
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                j1_CIMA = False
            if e.key == pygame.K_DOWN:
                j1_BAIXO = False

    desenho()
    bolaMovimento()
    mov_jogador()
    mov_jogador2()
    pygame.display.update()