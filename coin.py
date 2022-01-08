import pygame
import random

from gameObject import GameObject

class Coin(GameObject):
    def __init__(self, x, y, width, height, image, game):
        super().__init__(x, y, width, height, image, game)
        self.x = random.randint(0, self.game.window.width - self.width)
        self.y = random.randint(0, self.game.window.height - self.height)
        self.mask = pygame.mask.from_surface(self.image)
