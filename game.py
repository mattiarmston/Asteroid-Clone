import pygame
import time

from window import Window
from assets import Assets
from player import Player
from asteroid import Asteroid
from coin import Coin

class Game():
    def __init__(self):
        self.window = Window(self)
        self.assets = Assets(self.window, self)
        self.run = True
        self.lost = False
        self.FPS = 15
        self.toDraw = []
        self.framesPassed = 0
        self.timeAlive = 0
        self.clock = pygame.time.Clock()
        self.score = 0
        self.highscore = -1
        self.longestTime = -1
        self.coinSpawned = False
        self.asteroidSpawnRate = 30
        self.mainFont = pygame.font.SysFont("monospace", 40, bold=True)

    def takeInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
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
            35,
            35,
            self.assets.playerImage,
            self,
            1
        )
        self.toDraw.append(self.player)
        self.lost = False

    def menuScreen(self):
        def getName():
            name = ''
            for letter in letters:
                name += letter
            self.name = name

        self.name = ''
        letters = []
        self.window.menuScreen()
        nonText = [pygame.K_TAB, pygame.K_CLEAR, pygame.K_RETURN, pygame.K_PAUSE, pygame.K_ESCAPE,
                pygame.K_CAPSLOCK, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT,
                pygame.K_INSERT, pygame.K_HOME, pygame.K_END, pygame.K_PAGEUP, pygame.K_PAGEDOWN]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif pygame.key.get_pressed()[pygame.K_RETURN]:
                    getName()
                    return self.name
                elif event.type == pygame.KEYDOWN:
                    if event.mod & pygame.KMOD_LSHIFT:
                        keypressed = pygame.key.name(event.key)
                        letters.append(keypressed.upper())
                        if letters[-1] == 'LEFT SHIFT':
                            letters.pop()
                    if event.mod & pygame.KMOD_RSHIFT:
                        keypressed = pygame.key.name(event.key)
                        letters.append(keypressed.upper())
                        if letters[-1] == 'RIGHT SHIFT':
                            letters.pop()
                    elif event.key == pygame.K_SPACE:
                        letters.append(' ')
                    elif event.key in nonText:
                        pass
                    elif pygame.key.get_mods() & event.mod:
                        if event.key == pygame.K_BACKSPACE and event.mod & pygame.KMOD_CTRL:
                            # for letter in letters:
                            #     letters.pop()
                            letters = []
                    elif pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                        try:
                            letters.pop()
                        except:
                            pass
                    else:
                        keypressed = pygame.key.name(event.key)
                        letters.append(keypressed)
            getName()
            self.window.menuScreen()

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

    def endScreen(self, playerName):
        bufferheight = 5
        self.endTime = time.time()
        self.timeAlive = self.endTime - self.startTime
        if self.score > self.highscore:
            self.highscore = self.score
        if self.timeAlive > self.longestTime:
            self.longestTime = self.timeAlive
        self.window.endScreen(self.timeAlive, playerName)

    def main(self, playerName):
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
        self.endScreen(playerName)
        time.sleep(2)
        self.window.menuScreen()

    def mainMenu(self):
        playerName = self.menuScreen()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                self.main(playerName)
