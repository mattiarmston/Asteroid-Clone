import pygame
import os

class Assets():
    def __init__(self, window, game):
        self.game = game
        self.BackgroundImage = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "background.png")),
            (window.width, window.height)
        )
        self.playerThrustAnim = [
            pygame.image.load(
                os.path.join("assets", "player1.png")),
            pygame.image.load(
                os.path.join("assets", "player2.png")),
        ]
        self.explosionAnim = [
            pygame.image.load(
                os.path.join("assets", "explosion1.png")),
            pygame.image.load(
                os.path.join("assets", "explosion2.png")),
            pygame.image.load(
                os.path.join("assets", "explosion3.png")),
            pygame.image.load(
                os.path.join("assets", "explosion4.png")),
            pygame.image.load(
                os.path.join("assets", "explosion5.png")),
            pygame.image.load(
                os.path.join("assets", "explosion6.png")),
            pygame.image.load(
                os.path.join("assets", "explosion7.png")),
            pygame.image.load(
                os.path.join("assets", "explosion8.png")),
            pygame.image.load(
                os.path.join("assets", "explosion9.png")),
        ]
        self.playerSmokeAnim = [
            pygame.image.load(
                os.path.join("assets", "playerSmoke1.png")),
            pygame.image.load(
                os.path.join("assets", "playerSmoke2.png")),
            pygame.image.load(
                os.path.join("assets", "playerSmoke3.png")),
            pygame.image.load(
                os.path.join("assets", "playerSmoke4.png")),
            pygame.image.load(
                os.path.join("assets", "playerSmoke5.png")),
            pygame.image.load(
                os.path.join("assets", "playerSmoke6.png")),
        ]
        self.asteroidImage = pygame.image.load(
            os.path.join("assets", "asteroid.png"))
        self.coinImage = pygame.image.load(
            os.path.join("assets", "jerry_can.png"))
        self.fullBox = pygame.image.load(
            os.path.join("assets", "whiteBox.png"))
        self.hollowBox = pygame.image.load(
            os.path.join("assets", "hollowBox.png"))
        # Replace with custom pixel font
        self.mainFont = pygame.font.Font("assets/PixelifyCustom.otf", 40)
        # This uses pygame to emulate bold fonts. It looks good enough and means
        # I don't have to do this manually.
        self.smallBoldFont = pygame.font.Font("assets/PixelifyCustom.otf", 40)
        self.smallBoldFont.bold = True
        self.boldFont = pygame.font.Font("assets/PixelifyCustom.otf", 50)
        self.boldFont.bold = True
        self.titleFont = pygame.font.Font("assets/PixelifyCustom.otf", 100)
        self.titleFont.bold = True
        pygame.mouse.set_visible(False)
