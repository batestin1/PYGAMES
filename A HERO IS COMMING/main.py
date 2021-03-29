import pygame
from Game import Game


class Main:

    def __init__(self):

        self.window = pygame.display.set_mode([1280, 720])
        self.title = pygame.display.set_caption("Platform")

        self.loop = True
        self.fps = pygame.time.Clock()

        self.game = Game()

    def draw(self):
        self.game.draw(self.window)
        self.game.update()

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            self.game.player.events(events)

    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pygame.display.update()


Main().update()
