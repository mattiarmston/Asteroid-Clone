import pygame

from gameObject import GameObject
from asteroid import Asteroid
from coin import Coin

class Player(GameObject):
    def __init__(self, x, y, width, height, image, game, acceleration):
        super().__init__(x, y, width, height, image, game)
        self.speedY = 0
        self.speedX = 0
        self.acceleration = acceleration
        self.mask = pygame.mask.from_surface(self.image)

    def moveSelf(self):
        if self.game.keys[pygame.K_w]:
            self.speedY -= self.acceleration
        if self.game.keys[pygame.K_s]:
            self.speedY += self.acceleration
        if self.game.keys[pygame.K_a]:
            self.speedX -= self.acceleration
        if self.game.keys[pygame.K_d]:
            self.speedX += self.acceleration
        if self.y + self.speedY + self.height > self.game.window.height:
            self.y = self.game.window.height - self.height
            self.speedY = 0
        elif self.y + self.speedY < 0:
            self.y = 0
            self.speedY = 0
        else:
            self.y += self.speedY
        if self.x + self.speedX + self.width > self.game.window.width:
            self.x = self.game.window.width - self.width
            self.speedX = 0
        elif self.x + self.speedX < 0:
            self.x = 0
            self.speedX = 0
        else:
            self.x += self.speedX

    def checkCollision(self):
        for item in self.game.toDraw:
            offsetX = item.x - self.x
            offsetY = item.y - self.y
            if self.mask.overlap(item.mask, (offsetX, offsetY)) != None:
                if type(item) == Asteroid:
                    self.game.lost = True
                elif type(item) == Coin:
                    self.game.score += 1
                    self.game.toDraw.remove(item)
                    self.game.coinSpawned = False
