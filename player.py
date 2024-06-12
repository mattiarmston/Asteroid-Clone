import math
import pygame

from gameObject import GameObject
from asteroid import Asteroid
from coin import Coin

class Player(GameObject):
    def __init__(self, x, y, width, height, image, game, thrust):
        super().__init__(x, y, width, height, image, game)
        self.speedY = 0
        self.speedX = 0
        self.thrust = thrust
        self.imageEast = self.image
        self.maxfuel = 10 * self.game.window.FPS
        self.fuel = self.maxfuel

    def moveSelf(self):
        self.updatePos()
        self.clampPos()
        self.updateDir()
        self.updateFuel()

    def updatePos(self):
        # This assumes constant acceleration and as of 12/6/24 this is true.
        # If this changes, integrals will need to be used to calculate the exact
        # area under the curve.
        accelX, accelY = 0, 0
        if self.game.keys[pygame.K_w] or self.game.keys[pygame.K_UP]:
            accelY -= self.thrust
        if self.game.keys[pygame.K_s] or self.game.keys[pygame.K_DOWN]:
            accelY += self.thrust
        if self.game.keys[pygame.K_a] or self.game.keys[pygame.K_LEFT]:
            accelX -= self.thrust
        if self.game.keys[pygame.K_d] or self.game.keys[pygame.K_RIGHT]:
            accelX += self.thrust
        # Area of a parallelogram: height = deltaTime, side a = speedX,
        # side b = speedX + accel * deltaTime.
        self.x += (self.speedX + accelX/2 * self.game.deltaTime) * self.game.deltaTime
        self.y += (self.speedY + accelY/2 * self.game.deltaTime) * self.game.deltaTime
        self.speedX += accelX * self.game.deltaTime
        self.speedY += accelY * self.game.deltaTime
        return

    def clampPos(self):
        if self.x < 0 or self.x > self.game.window.width - self.height:
            self.speedX = 0
        if self.y < 0 or self.y > self.game.window.height - self.height:
            self.speedY = 0
        self.x = min(max(0, self.x), self.game.window.width - self.height)
        self.y = min(max(0, self.y), self.game.window.height - self.height)
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
