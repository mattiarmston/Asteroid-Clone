import pygame
import random

from gameObject import GameObject

class Asteroid(GameObject):
    def __init__(self, width, height, speedX, speedY, image, game, x=0, y=0):
        super().__init__(x, y, width, height, image, game)
        self.speedX = speedX
        self.speedY = speedY
        self.mask = pygame.mask.from_surface(self.image)
        #Sets x and y position and ensures asteroids move onto screen
        self.spawnLocation()

    @staticmethod
    def spawnAsteroid(game):
        if game.framesPassed % game.asteroidSpawnRate == 0:
            asteroid = Asteroid(
                50, 50, random.randint(-15, 15), random.randint(-15,15),
                game.assets.asteroidImage, game
            )
            game.toDraw.append(asteroid)

    def spawnLocation(self):
        #Decides whether asteroid spaws on left/right or top/bottom edge of the screen
        if random.randint(0,1) == 1:
            #Asteroid spawns on left/right side of the screen
            if random.randint(0,1) == 1:
                #Asteroid spawns on left side of screen
                self.x = 0 - self.width
                self.y = random.randint(
                    int(self.game.window.height/2), int(self.game.window.height * 3/4))
                self.speedX = random.randint(1, 15)
            else:
                #Asteroid spawns on the right side of the screen
                self.x = self.game.window.width + self.width
                self.y = random.randint(
                    int(self.game.window.height/2), int(self.game.window.height * 3/4))
                self.speedX = random.randint(-15, -1)
        else:
            #Asteroid spawns on top/bottom side of the screen
            if random.randint(0,1) == 1:
                #Asteroid spawns on top side of the screen
                self.x = random.randint(
                    int(self.game.window.width/2), int(self.game.window.width * 3/4))
                self.y = 0 - self.height
                self.speedY = random.randint(1, 15)
            else:
                #Asteroid spawns on bottom side of the screen
                self.x = random.randint(
                    int(self.game.window.width/2), int(self.game.window.width * 3/4))
                self.y = self.game.window.height + self.height
                self.speedY = random.randint(-15, -1)

    def moveSelf(self):
        self.x += self.speedX
        self.y += self.speedY
