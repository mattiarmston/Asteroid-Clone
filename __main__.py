import pygame
import os
import time
import random
pygame.init()

#Setting up window
WIDTH, HEIGHT = 750, 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top down shooter")

#Setting up images
BackgroundImage = pygame.transform.scale(pygame.image.load(os.path.join("assets", "blankBG.png")), (WIDTH, HEIGHT))
playerImage = pygame.image.load(os.path.join("assets", "playerImage.png"))
asteroidImage = pygame.image.load(os.path.join("assets", "asteroidImage.png"))

class Game():
    def __init__(self):
        self.run = True
        self.FPS = 120
        self.framesPassed = 0
        self.clock = pygame.time.Clock()
        self.score = 0
    def drawFrame(self):
        WINDOW.blit(BackgroundImage, (0,0))
        for item in toDraw:
            WINDOW.blit(item.image, (item.x, item.y))
        pygame.display.update()
    def takeInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        self.keys = pygame.key.get_pressed()
    def main(self):
        while self.run:
            self.clock.tick(self.FPS)
            #Used for spawning x asteroids per second. Need to find better solution.
            self.framesPassed += 1
            self.score += 1
            if self.framesPassed > self.FPS:
                self.framesPassed = 0
            masteroid.spawnAsteroid()
            self.drawFrame()
            self.takeInputs()
            for item in toDraw:
                item.moveSelf()
            player.hitAsteroid()

class Player():
    def __init__(self, x, y, width, height, speed, acceleration, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.acceleration
        self.image = pygame.transform.scale(playerImage, (self.width, self.height))
        self.mask = pygame.mask.from_surface(self.image)
    def moveSelf(self):
        if game.keys[pygame.K_w] and self.y - self.speed > 0:
            self.y -= self.speed
        if game.keys[pygame.K_s] and self.y + self.speed + self.height < HEIGHT:
            self.y += self.speed
        if game.keys[pygame.K_a] and self.x - self.speed > 0:
            self.x -= self.speed
        if game.keys[pygame.K_d] and self.x + self.speed + self.width < WIDTH:
            self.x += self.speed
    def hitAsteroid(self):
        for item in toDraw:
            offsetX = item.x - self.x
            offsetY = item.y - self.y
            if self.mask.overlap(item.mask, (offsetX, offsetY)) != None:
                if item.mask != self.mask:
                    print("Your score is {}".format(game.score))
                    game.run = False

class Asteroid():
    def __init__(self, width, height, speedX, speedY, image, masteroid):
        self.width = width
        self.height = height
        self.speedX = speedX
        self.speedY = speedY
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.masteroid = masteroid
        if self.masteroid:
            self.x = WIDTH * 2
            self.y = HEIGHT * 2
        else:
            #Sets x and y position and ensures asteroids move onto screen
            self.spawnLocation()
    def spawnAsteroid(self):
        if game.framesPassed % 60 == 0:
            asteroid = Asteroid(50, 50, random.randint(-15, 15), random.randint(-15,15), asteroidImage, False)
            toDraw.append(asteroid)
    def spawnLocation(self):
        #Decides whether asteroid spaws on left/right or top/bottom edge of the screen
        if random.randint(0,1) == 1:
            #Asteroid spawns on left/right side of the screen
            if random.randint(0,1) == 1:
                #Asteroid spawns on left side of screen
                self.x = 0 - self.width
                self.y = random.randint(0, HEIGHT)
                self.speedX = random.randint(1, 15)
            else:
                #Asteroid spawns on the right side of the screen
                self.x = WIDTH + self.width
                self.y = random.randint(0, HEIGHT)
                self.speedX = random.randint(-15, -1)
        else:
            #Asteroid spawns on top/bottom side of the screen
            if random.randint(0,1) == 1:
                #Asteroid spawns on top side of the screen
                self.x = random.randint(0, WIDTH)
                self.y = 0 - self.height
                self.speedY = random.randint(1, 15)
            else:
                #Asteroid spawns on bottom side of the screen
                self.x = random.randint(0, WIDTH)
                self.y = HEIGHT + self.height
                self.speedY = random.randint(-15, -1)
    def moveSelf(self):
        self.x += self.speedX
        self.y += self.speedY
        
toDraw = []
player = Player(int(WIDTH/2), int(HEIGHT/2), 35, 35, 10, 1, playerImage)
masteroid = Asteroid(50, 50, 0, 0, asteroidImage, True)
toDraw.append(player)
game = Game()
game.main()
