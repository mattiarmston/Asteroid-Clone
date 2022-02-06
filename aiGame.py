import pygame
import time

from window import Window
from assets import Assets
from player import Player
from asteroid import Asteroid
from coin import Coin

class Game():
    def __init__(self):
        self.window = Window()
        self.assets = Assets(self.window)
        self.run = True
        self.lost = False
        self.FPS = 15
        self.toDraw = []
        self.framesPassed = 0
        self.timeAlive = 0
        self.clock = pygame.time.Clock()
        self.score = 0
        self.coinSpawned = False
        self.asteroidSpawnRate = 30
        self.mainFont = pygame.font.SysFont("comicsans", 70)

    def drawFrame(self):
        self.window.window.blit(self.assets.BackgroundImage, (0,0))
        for item in self.toDraw:
            self.window.window.blit(item.image, (item.x, item.y))
        scoreLabel = self.mainFont.render("Score: {}".format(self.score),
                     1, (255, 255, 255))
        timeLabel = self.mainFont.render("Time: {}".format(self.timeAlive),
                    1, (255, 255, 255))
        self.window.window.blit(scoreLabel, (20, 20))
        self.window.window.blit(timeLabel, (self.window.width-timeLabel.get_width() - 20, 20))
        pygame.display.update()

    def takeInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        self.keys = pygame.key.get_pressed()

    def initGame(self):
        self.genomes = []
        self.nets = []
        self.toDraw = []
        self.score = 0
        self.framesPassed= 0
        self.coinSpawned = False
        self.asteroidSpawnRate = 30
        self.player = Player(int(self.window.width/2), int(self.window.height/2), 35, 35, self.assets.playerImage, self, 1)
        self.toDraw.append(self.player)
        self.lost = False

    def spawnObjects(self):
        #Used for spawning x asteroids per second. Need to find better solution.
        self.framesPassed += 1
        if self.framesPassed == self.FPS:
            self.framesPassed = 0
        Asteroid.spawnAsteroid(self)
        if self.coinSpawned == False:
            coin = Coin(0, 0, 30, 30, self.assets.coinImage, self)
            self.coinSpawned = True
            self.toDraw.append(coin)

    def increaseDifficulty(self):
        self.currentTimeS = int(time.strftime("%S", time.localtime()))
        self.currentTimeM = int(time.strftime("%M", time.localtime()))
        self.currentTime = self.currentTimeM * 60 + self.currentTimeS
        self.timeAlive = self.currentTime - self.startTime
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
        elif self.timeAlive > 15 and self.timeAlive % 5 == 0:
            if self.framesPassed == 0 and self.asteroidSpawnRate > 1:
                self.asteroidSpawnRate -= 1
                print("Asteroid", self.asteroidSpawnRate)

    def menuScreen(self):
        self.window.window.blit(self.assets.BackgroundImage, (0,0))
        startText = self.mainFont.render("Press space to play", 1, (255, 255, 255))
        self.window.window.blit(
            startText,
            (self.window.width/2 - startText.get_width()/2, self.window.height/2 - startText.get_height()/2)
        )
        pygame.display.update()

    def endScreen(self):
        self.endTimeS = int(time.strftime("%S", time.localtime()))
        self.endTimeM = int(time.strftime("%M", time.localtime()))
        self.endTime = self.endTimeM * 60 + self.endTimeS
        self.timeAlive = self.endTime - self.startTime
        scoreText = self.mainFont.render(
            "Your score is {}".format(self.score),
            1, (255, 255, 255)
        )
        timeText = self.mainFont.render(
            "You survived for {} seconds".format(self.timeAlive),
            1, (255, 255, 255)
        )
        self.window.window.blit(
            scoreText,
            (self.window.width/2 - scoreText.get_width()/2,
            self.window.height/2 - scoreText.get_height()/2)
        )
        self.window.window.blit(
            timeText,
            (self.window.width/2 - timeText.get_width()/2, self.window.height/2 - scoreText.get_height() - timeText.get_height()/2)
        )
        pygame.display.update()

    def fitness():
        fitness = self.score * 10 + self.timeAlive
        return fitness

    def eval_genomes(self, genomes):
        self.initGame()
        self.startTimeS = int(time.strftime("%S", time.localtime()))
        self.startTimeM = int(time.strftime("%M", time.localtime()))
        self.startTime = self.startTimeM * 60 + self.startTimeS
        while self.lost == False:
            self.clock.tick(self.FPS)
            self.spawnObjects()
            self.takeInputs()
            for item in self.toDraw:
                item.moveSelf()
            self.player.checkCollision()
            self.increaseDifficulty()
            self.drawFrame()
        self.endScreen()
        time.sleep(2)
        self.menuScreen()

    def mainMenu(self):
        pygame.mouse.set_visible(False)
        self.menuScreen()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.main()
