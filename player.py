import math
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
        self.imageEast = self.image
        self.maxfuel = 10 * self.game.window.FPS
        self.fuel = self.maxfuel

    def moveSelf(self):
        self.updatePos()
        self.updateDir()
        self.updateFuel()

    def updatePos(self):
        if self.game.keys[pygame.K_w] or self.game.keys[pygame.K_UP]:
            self.speedY -= self.acceleration
        if self.game.keys[pygame.K_s] or self.game.keys[pygame.K_DOWN]:
            self.speedY += self.acceleration
        if self.game.keys[pygame.K_a] or self.game.keys[pygame.K_LEFT]:
            self.speedX -= self.acceleration
        if self.game.keys[pygame.K_d] or self.game.keys[pygame.K_RIGHT]:
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
        return

    def updateDir(self):
        # The trigonometry here assumes that a positive dY means an upward,
        # moving player.
        speedY = self.speedY * -1
        if self.speedX == 0:
            if speedY < 0:
                theta = -90
            else:
                theta = 90
        else:
            thetaRad = math.atan(speedY / self.speedX)
            theta = math.degrees(thetaRad)
            if self.speedX < 0:
                theta += 180
        self.image = pygame.transform.rotate(self.imageEast, theta)
        return

    def updateFuel(self):
        self.fuel -= 1
        if self.fuel < 1:
            self.game.playerDead()

    def checkCollision(self):
        for item in self.game.toDraw:
            offsetX = item.x - self.x
            offsetY = item.y - self.y
            if self.mask.overlap(item.mask, (offsetX, offsetY)) != None:
                if type(item) == Asteroid:
                    self.game.playerDead()
                elif type(item) == Coin:
                    self.fuel = self.maxfuel
                    self.game.score += 1
                    self.game.toDraw.remove(item)
                    self.game.coinSpawned = False
