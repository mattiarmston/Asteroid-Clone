import pygame

class GameObject():
    def __init__(self, x, y, width, height, image, game):
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.image = pygame.transform.scale(image, (self.width, self.height))
       self.game = game

    def moveSelf(self):
        pass

    def onCollision(self):
        pass
