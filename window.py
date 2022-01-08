import pygame

class Window():
    def __init__(self):
        self.width, self.height = 1000, 1000
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Asteroid clone")
