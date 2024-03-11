import json
import pygame
import time

from window import Window
from assets import Assets
from player import Player
from asteroid import Asteroid
from coin import Coin

class Game():
    def __init__(self, scores):
        self.window = Window(self)
        self.assets = Assets(self.window, self)
        self.lost = False
        self.FPS = 15
        self.toDraw = []
        self.framesPassed = 0
        self.timeAlive = 0
        self.clock = pygame.time.Clock()
        self.scores = scores
        self.score = 0
        self.highscore = self.getHighscore()
        self.longestTime = -1
        self.coinSpawned = False
        self.asteroidSpawnRate = 30

    @staticmethod
    def getScore(entry):
        print(entry)
        print(entry[2])
        return entry[2]

    def getHighscore(self):
        if self.scores == []:
            return 0
        print("pre", self.scores)
        self.scores.sort(key=self.getScore)
        print("post", self.scores)
        return self.scores[-1][2]

    def takeInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quitGame()
        self.keys = pygame.key.get_pressed()

    def initGame(self):
        self.toDraw = []
        self.score = 0
        self.framesPassed= 0
        self.coinSpawned = False
        self.asteroidSpawnRate = 30
        self.player = Player(
            int(self.window.width/2),
            int(self.window.height/2),
            32,
            32,
            self.assets.playerImage,
            self,
            1
        )
        self.toDraw.append(self.player)
        self.lost = False

    def spawnObjects(self):
        #Used for spawning x asteroids per second. Need to find better solution.
        self.framesPassed += 1
        if self.framesPassed == self.FPS:
            self.framesPassed = 0
        Asteroid.spawnAsteroid(self)
        if self.coinSpawned == False:
            coin = Coin(0, 0, 32, 32, self.assets.coinImage, self)
            self.coinSpawned = True
            self.toDraw.append(coin)

    def increaseDifficulty(self):
        self.currentTime = time.time()
        self.timeAlive = self.currentTime - self.startTime
        if int(self.timeAlive) == 5:
            # Ensures spawn rate is only decreased once, not every frame
            if self.framesPassed == 0:
                self.asteroidSpawnRate -= 5
                print("Asteroid", self.asteroidSpawnRate)
        elif int(self.timeAlive) == 10:
            if self.framesPassed == 0:
                self.asteroidSpawnRate -= 5
                print("Asteroid", self.asteroidSpawnRate)
        elif int(self.timeAlive) == 15:
            if self.framesPassed == 0:
                self.asteroidSpawnRate -= 5
                print("Asteroid", self.asteroidSpawnRate)
        elif int(self.timeAlive) > 15 and int(self.timeAlive) % 5 == 0:
            if self.framesPassed == 0 and self.asteroidSpawnRate > 1:
                self.asteroidSpawnRate -= 1
                print("Asteroid", self.asteroidSpawnRate)

    def playerDead(self):
        self.lost = True
        self.endTime = time.time()

    def endScreen(self):
        self.window.endScreen()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
        return

    def enterName(self):
        playerName = ''
        pygame.key.start_text_input()
        done = False
        while not done:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
                    if event.key == pygame.K_BACKSPACE:
                        if event.mod & pygame.KMOD_CTRL:
                            playerName = ''
                        else:
                            playerName = playerName[:-1]
                if event.type == pygame.TEXTINPUT:
                    playerName += event.text
            self.window.enterName(playerName)
        pygame.key.stop_text_input()
        return playerName

    def setHighscore(self, playerName):
        self.timeAlive = self.endTime - self.startTime
        if self.score > self.highscore:
            self.highscore = self.score
        if self.timeAlive > self.longestTime:
            self.longestTime = self.timeAlive
        self.scores.append([playerName, self.timeAlive, self.score])
        self.scores.sort(key=self.getScore)

    def help(self):
        self.window.help()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
        return

    def quitGame(self):
        with open("highscores.json", "w") as file:
            jsonString = json.dumps(self.scores)
            file.write(jsonString)
            file.write("\n")
        quit()

    def main(self):
        self.initGame()
        self.startTime = time.time()
        while self.lost == False:
            self.clock.tick(self.FPS)
            self.spawnObjects()
            self.takeInputs()
            for item in self.toDraw:
                item.moveSelf()
            self.player.checkCollision()
            self.increaseDifficulty()
            self.window.drawFrame()
        self.endScreen()
        playerName = self.enterName()
        self.setHighscore(playerName)
        return

    def mainMenu(self):
        while True:
            confirmed = False
            selected = 0
            options = [self.main, self.help]
            while not confirmed:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quitGame()
                    if event.type == pygame.KEYDOWN:
                        if event.key in [pygame.K_UP, pygame.K_w]:
                            selected -= 1
                            selected = max(selected, 0)
                        if event.key in [pygame.K_DOWN, pygame.K_s]:
                            selected += 1
                            selected = min(selected, len(options))
                        if event.key == pygame.K_RETURN:
                            confirmed = True
                self.window.mainMenu(selected)
            options[selected]()
