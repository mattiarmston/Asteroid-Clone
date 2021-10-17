import pygame
import os
import time
import random
pygame.init()

#Setting up window
WIDTH, HEIGHT = 1000, 1000
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroid clone")

#Setting up images
BackgroundImage = pygame.transform.scale(pygame.image.load(os.path.join("assets", "blankBG.png")), (WIDTH, HEIGHT))
playerImage = pygame.image.load(os.path.join("assets", "playerImage.png"))
asteroidImage = pygame.image.load(os.path.join("assets", "asteroidImage.png"))
coinImage = pygame.image.load(os.path.join("assets", "coinImage.png"))

class Game():
    def __init__(self):
        self.run = True
        self.lost = False
        self.FPS = 15
        self.toDraw = []
        self.framesPassed = 0
        self.secondsPassed = 0
        self.clock = pygame.time.Clock()
        self.score = 0
        self.coinSpawned = False
        self.asteroidSpawnRate = 30
        self.mainFont = pygame.font.SysFont("comicsans", 70)
    def drawFrame(self):
        WINDOW.blit(BackgroundImage, (0,0))
        for item in self.toDraw:
            WINDOW.blit(item.image, (item.x, item.y))
        pygame.display.update()
    def takeInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        self.keys = pygame.key.get_pressed()
    def initGame(self):
        self.toDraw = []
        self.score = 0
        self.framesPassed, self.secondsPassed = 0, 0
        self.coinSpawned = False
        self.asteroidSpawnRate = 30
        self.player = Player(int(WIDTH/2), int(HEIGHT/2), 35, 35, "player", playerImage, 1)
        self.toDraw.append(self.player)
        self.lost = False
    def spawnObjects(self):
        #Used for spawning x asteroids per second. Need to find better solution.
        self.framesPassed += 1
        if self.framesPassed == self.FPS:
            self.framesPassed = 0
            self.secondsPassed += 1
        Asteroid.spawnAsteroid()
        if self.coinSpawned == False:
            coin = Coin(0, 0, 30, 30, "coin", coinImage)
            self.coinSpawned = True
            self.toDraw.append(coin)
    def increaseDifficulty(self):
        self.currentTimeS = int(time.strftime("%S", time.localtime()))
        self.currentTimeM = int(time.strftime("%M", time.localtime()))
        self.currentTime = self.currentTimeM * 60 + self.currentTimeS
        self.timeAlive = self.currentTime - self.startTime
        print(self.timeAlive)
        if self.timeAlive == 5:
            #Ensures spawn rate is only decreased once, not every frame
            if self.framesPassed == 0:
                self.asteroidSpawnRate -= 5
                print("Asteroid", self.asteroidSpawnRate)
        elif self.timeAlive == 10:
            if self.framesPassed == 0:
                self.asteroidSpawnRate -= 5
                print("Asteroid", self.asteroidSpawnRate)
        elif self.timeAlive == 15:
            if self.framesPassed == 0:
                self.asteroidSpawnRate -= 5
                print("Asteroid", self.asteroidSpawnRate)
        elif self.timeAlive > 15 and self.secondsPassed % 5 == 0:
            if self.framesPassed == 0 and self.asteroidSpawnRate > 1:
                self.asteroidSpawnRate -= 1
                print("Asteroid", self.asteroidSpawnRate)
    def main(self):
        self.initGame()
        self.startTimeS = int(time.strftime("%S", time.localtime()))
        self.startTimeM = int(time.strftime("%M", time.localtime()))
        self.startTime = self.startTimeM * 60 + self.startTimeS
        while self.lost == False:
            self.clock.tick(self.FPS)
            self.spawnObjects()
            self.drawFrame()
            self.takeInputs()
            for item in self.toDraw:
                item.moveSelf()
            self.player.onCollision()
            self.increaseDifficulty()
        self.endTimeS = int(time.strftime("%S", time.localtime()))
        self.endTimeM = int(time.strftime("%M", time.localtime()))
        self.endTime = self.endTimeM * 60 + self.endTimeS
        self.timeAlive = self.endTime - self.startTime
        scoreText = self.mainFont.render("Your score is {}".format(self.score),
                    1, (255, 255, 255))
        timeText = self.mainFont.render("You survived for {} seconds".format(self.timeAlive),
                   1, (255, 255, 255))
        WINDOW.blit(scoreText, (WIDTH/2 - scoreText.get_width()/2,
                    HEIGHT/2 - scoreText.get_height()/2))
        WINDOW.blit(timeText, (WIDTH/2 - timeText.get_width()/2,
                    HEIGHT/2 - scoreText.get_height() - timeText.get_height()/2))
        pygame.display.update()
        time.sleep(2)
    def mainMenu(self):
        while self.run:
            self.main()

class Object():
    def __init__(self, x, y, width, height, child, image):
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.child = child
       self.image = pygame.transform.scale(image, (self.width, self.height))
    def moveSelf(self):
        pass
    def onCollision(self):
        pass

class Player(Object):
    def __init__(self, x, y, width, height, child, image, acceleration):
        super().__init__(x, y, width, height, child, image)
        self.speedY = 0
        self.speedX = 0
        self.acceleration = acceleration
        self.mask = pygame.mask.from_surface(self.image)
    def moveSelf(self):
        if game.keys[pygame.K_w]:
            self.speedY -= self.acceleration
        if game.keys[pygame.K_s]:
            self.speedY += self.acceleration
        if game.keys[pygame.K_a]:
            self.speedX -= self.acceleration
        if game.keys[pygame.K_d]:
            self.speedX += self.acceleration
        if self.y + self.speedY + self.height > HEIGHT:
            self.y = HEIGHT - self.height
            self.speedY = 0
        elif self.y + self.speedY < 0:
            self.y = 0
            self.speedY = 0
        else:
            self.y += self.speedY
        if self.x + self.speedX + self.width > WIDTH:
            self.x = WIDTH - self.width
            self.speedX = 0
        elif self.x + self.speedX < 0:
            self.x = 0
            self.speedX = 0
        else:
            self.x += self.speedX
    def onCollision(self):
        for item in game.toDraw:
            offsetX = item.x - self.x
            offsetY = item.y - self.y
            if self.mask.overlap(item.mask, (offsetX, offsetY)) != None:
                if item.child == "asteroid":
                    game.lost = True
                if item.child == "coin":
                    game.score += 1
                    game.toDraw.remove(item)
                    game.coinSpawned = False

class Asteroid(Object):
    def __init__(self, width, height, child, speedX, speedY, image, x=0, y=0):
        super().__init__(x, y, width, height, child, image)
        self.speedX = speedX
        self.speedY = speedY
        self.mask = pygame.mask.from_surface(self.image)
        #Sets x and y position and ensures asteroids move onto screen
        self.spawnLocation()
    def spawnAsteroid():
        if game.framesPassed % game.asteroidSpawnRate == 0:
            asteroid = Asteroid(50, 50, "asteroid",
                    random.randint(-15, 15), random.randint(-15,15), asteroidImage)
            game.toDraw.append(asteroid)
    def spawnLocation(self):
        #Decides whether asteroid spaws on left/right or top/bottom edge of the screen
        if random.randint(0,1) == 1:
            #Asteroid spawns on left/right side of the screen
            if random.randint(0,1) == 1:
                #Asteroid spawns on left side of screen
                self.x = 0 - self.width
                self.y = random.randint(int(HEIGHT/2), int(HEIGHT * 3/4))
                self.speedX = random.randint(1, 15)
            else:
                #Asteroid spawns on the right side of the screen
                self.x = WIDTH + self.width
                self.y = random.randint(int(HEIGHT/2), int(HEIGHT * 3/4))
                self.speedX = random.randint(-15, -1)
        else:
            #Asteroid spawns on top/bottom side of the screen
            if random.randint(0,1) == 1:
                #Asteroid spawns on top side of the screen
                self.x = random.randint(int(WIDTH/2), int(WIDTH * 3/4))
                self.y = 0 - self.height
                self.speedY = random.randint(1, 15)
            else:
                #Asteroid spawns on bottom side of the screen
                self.x = random.randint(int(WIDTH/2), int(WIDTH * 3/4))
                self.y = HEIGHT + self.height
                self.speedY = random.randint(-15, -1)
    def moveSelf(self):
        self.x += self.speedX
        self.y += self.speedY

class Coin(Object):
    def __init__(self, x, y, width, height, child, image):
        super().__init__(x, y, width, height, child, image)
        self.x = random.randint(0, WIDTH - self.width)
        self.y = random.randint(0, HEIGHT - self.height)
        self.mask = pygame.mask.from_surface(self.image)

        
game = Game()
game.mainMenu()
