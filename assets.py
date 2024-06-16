import pygame
import os

class Assets():
    def __init__(self, window, game):
        self.game = game
        self.BackgroundImage = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "background.png")),
            (window.width, window.height)
        )
        self.playerImage = pygame.image.load(
            os.path.join("assets", "player2.png"))
        self.asteroidImage = pygame.image.load(
            os.path.join("assets", "asteroid.png"))
        self.coinImage = pygame.image.load(
            os.path.join("assets", "jerry_can.png"))
        self.fullBox = pygame.image.load(
            os.path.join("assets", "whiteBox.png"))
        self.hollowBox = pygame.image.load(
            os.path.join("assets", "hollowBox.png"))
        self.mainFont = pygame.font.SysFont("monospace", 40)
        self.boldFont = pygame.font.SysFont("monospace", 40, bold=True)
        self.titleFont = pygame.font.SysFont("monospace", 80, bold=True)
        # Replace with custom pixel font
        self.mainFont = pygame.font.Font("assets/PixelifyCustom.otf", 40)
        # This uses pygame to emulate bold fonts. It looks good enough and means
        # I don't have to do this manually.
        self.boldFont = pygame.font.Font("assets/PixelifyCustom.otf", 50)
        self.boldFont.bold = True
        self.titleFont = pygame.font.Font("assets/PixelifyCustom.otf", 100)
        self.titleFont.bold = True
        pygame.mouse.set_visible(False)
