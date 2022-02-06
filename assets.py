import pygame
import os

class Assets():
    def __init__(self, window, game):
        self.game = game
        self.BackgroundImage = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "blankBG.png")),
            (window.width, window.height)
        )
        self.playerImage = pygame.image.load(os.path.join("assets", "playerImage.png"))
        self.asteroidImage = pygame.image.load(os.path.join("assets", "asteroidImage.png"))
        self.coinImage = pygame.image.load(os.path.join("assets", "coinImage.png"))
