import json
import pygame
import time

from assets import Assets
from asteroid import Asteroid
from coin import Coin
from player import Player
from settings import playerSettings
from sound import Sound
from window import Window

class Game():
    def __init__(self, scores):
        self.window = Window(self)
        self.assets = Assets(self.window, self)
        self.sound = Sound(self)
        self.playerSettings = playerSettings
        self.lost = False
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
            289,
        )
        self.toDraw.append(self.player)
        self.lost = False

    def takeInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quitGame()
        self.keys = pygame.key.get_pressed()

    def spawnObjects(self):
        #Used for spawning x asteroids per second. Need to find better solution.
        self.framesPassed += 1
        if self.framesPassed == self.window.FPS:
            self.framesPassed = 0
        Asteroid.spawnAsteroid(self)
        if self.coinSpawned == False:
            coin = Coin(0, 0, 32, 32, self.assets.coinImage, self)
            self.coinSpawned = True
            self.toDraw.append(coin)

    def increaseDifficulty(self):
        # Increase spawn rate only once
        if self.framesPassed != 0:
            return
        timeAlive = int(self.timeAlive)
        if timeAlive % 5 == 0:
            if timeAlive <= 15:
                self.asteroidSpawnRate = max(1, self.asteroidSpawnRate - 5)
            if timeAlive > 15: 
                self.asteroidSpawnRate = max(1, self.asteroidSpawnRate - 1)

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
            self.clock.tick(self.window.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if playerName.strip() != '':
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

    def getHighscore(self):
        if self.scores == []:
            return 0
        self.scores.sort(reverse=True, key=lambda e : e[2])
        return self.scores[0][2]

    def setHighscore(self, playerName):
        self.timeAlive = self.endTime - self.startTime
        if self.score > self.highscore:
            self.highscore = self.score
        if self.timeAlive > self.longestTime:
            self.longestTime = self.timeAlive
        self.scores.append([playerName, self.timeAlive, self.score])
        self.scores.sort(reverse=True, key=lambda e : e[2])

    def update(self):
        self.clock.tick(self.window.FPS)
        self.deltaTime = self.clock.get_time() / 1000
        self.timeAlive = time.time() - self.startTime
        self.spawnObjects()
        self.takeInputs()
        for item in self.toDraw:
            item.moveSelf()
        self.player.checkCollision()
        self.increaseDifficulty()
        self.window.drawFrame()

    def main(self):
        self.initGame()
        self.startTime = time.time()
        while self.lost == False:
            self.update()
        self.endScreen()
        playerName = self.enterName()
        self.setHighscore(playerName)
        return

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

    def viewHighscores(self):
        scores = self.scores[0:20]
        self.window.viewHighscores(scores)
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
        return

    def updateSettings(self):
        # When settings change get each module to update accordingly
        self.sound.updateSettings()
        return

    def settings(self):
        confirmed = False
        selected = 0
        options = ["music", "sound", "back"]
        while True:
            while not confirmed:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quitGame()
                    if event.type != pygame.KEYDOWN:
                        continue
                    if event.key in [pygame.K_UP, pygame.K_w]:
                        selected -= 1
                        selected = max(selected, 0)
                    if event.key in [pygame.K_DOWN, pygame.K_s]:
                        selected += 1
                        selected = min(selected, len(options) - 1)
                    if event.key == pygame.K_RETURN:
                        confirmed = True
                self.window.settings(selected, self.playerSettings)
            if options[selected] == "back":
                break
            self.playerSettings[options[selected]] = not self.playerSettings[options[selected]]
            self.updateSettings()
            confirmed = False

    def quitGame(self):
        with open("highscores.json", "w") as file:
            jsonString = json.dumps(self.scores)
            file.write(jsonString)
            file.write("\n")
        with open("settings.json", "w") as file:
            file.write(json.dumps(self.playerSettings))
            file.write("\n")
        quit()

    def mainMenu(self):
        self.sound.playMainLoop()
        while True:
            confirmed = False
            selected = 0
            options = [self.main, self.help, self.settings, self.viewHighscores]
            while not confirmed:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quitGame()
                    if event.type != pygame.KEYDOWN:
                        continue
                    if event.key in [pygame.K_UP, pygame.K_w]:
                        selected -= 1
                        selected = max(selected, 0)
                    if event.key in [pygame.K_DOWN, pygame.K_s]:
                        selected += 1
                        selected = min(selected, len(options) - 1)
                    if event.key == pygame.K_RETURN:
                        confirmed = True
                self.window.mainMenu(selected)
            options[selected]()
