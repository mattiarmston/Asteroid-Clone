import pygame

class Window():
    def __init__(self, game):
        self.game = game
        self.width, self.height = 1000, 1000
        self.window = pygame.display.set_mode((self.width, self.height))
        self.FPS = 60
        self.defaultCol = (255, 255, 255)
        pygame.display.set_caption("Asteroid clone")

    def mainMenu(self, selected):
        fonts = [self.game.assets.mainFont, self.game.assets.mainFont,
                 self.game.assets.mainFont, self.game.assets.mainFont]
        fonts[selected] = self.game.assets.boldFont
        i = 0
        playText = fonts[i].render(
            'Play',
            1, self.defaultCol
        )
        i += 1
        helpText = fonts[i].render(
            'Help',
            1, self.defaultCol
        )
        i += 1
        settingsText = fonts[i].render(
            'Settings',
            1, self.defaultCol
        )
        i += 1
        highscoresText = fonts[i].render(
            'Highscores',
            1, self.defaultCol
        )
        i += 1
        self.window.blit(self.game.assets.BackgroundImage, (0,0))
        y = self.height / 4
        self.window.blit(
            playText,
            (self.width / 2 - playText.get_width() / 2, y)
        )
        y += playText.get_height() * 3
        self.window.blit(
            helpText,
            (self.width / 2 - helpText.get_width() / 2, y)
        )
        y += helpText.get_height() * 3
        self.window.blit(
            settingsText,
            (self.width / 2 - settingsText.get_width() / 2, y)
        )
        y += settingsText.get_height() * 3
        self.window.blit(
            highscoresText,
            (self.width / 2 - highscoresText.get_width() / 2, y)
        )
        y += highscoresText.get_height() * 3
        pygame.display.update()

    def help(self):
        controlsText = self.game.assets.mainFont.render(
            "Use WASD or Arrow Keys to move.",
            1, self.defaultCol
        )
        objectiveText = self.game.assets.mainFont.render(
            "Avoid Asteroids and collect fuel",
            1, self.defaultCol
        )
        objectiveText2 = self.game.assets.mainFont.render(
            "to survive as long as possible",
            1, self.defaultCol
        )
        backText = self.game.assets.boldFont.render(
            "Back",
            1, self.defaultCol
        )
        self.window.blit(self.game.assets.BackgroundImage, (0,0))
        self.window.blit(
            controlsText,
            (self.width/2 - controlsText.get_width()/2,
            self.height/3)
        )
        self.window.blit(
            objectiveText,
            (self.width/2 - objectiveText.get_width()/2,
            self.height/3 + controlsText.get_height())
        )
        self.window.blit(
            objectiveText2,
            (self.width/2 - objectiveText2.get_width()/2,
            self.height/3 + controlsText.get_height()+objectiveText.get_height())
        )
        self.window.blit(
            backText,
            (self.width/2 - backText.get_width()/2,
            self.height/3 + controlsText.get_height() + \
                objectiveText.get_height() + objectiveText2.get_height() * 2)
        )
        pygame.display.update()

    def viewHighscores(self, scores):
        titleText = self.game.assets.mainFont.render(
            # Whitespace for formatting
            "    Name           Time       Score",
            1, self.defaultCol
        )
        backText = self.game.assets.boldFont.render(
            "Back",
            1, self.defaultCol
        )
        self.window.blit(self.game.assets.BackgroundImage, (0,0))
        x = 30
        y = 30
        self.window.blit(
            titleText,
            (x,
            y)
        )
        y += titleText.get_height() + 10
        i = 1
        for score in scores:
            text = self.game.assets.mainFont.render(
                "{num:>2}. {name:<14} {time:<10.2f} {score:>5}".format(
                    name=score[0][0:14], num=i, time=score[1], score=score[2]),
                1, self.defaultCol
            )
            self.window.blit(text, (x,y))
            y += text.get_height()
            i += 1
        self.window.blit(
            backText, (self.width/2 - backText.get_width()/2, y + 30))
        pygame.display.update()

    def settings(self, selected, settings):
        self.window.blit(self.game.assets.BackgroundImage, (0,0))
        fonts = [self.game.assets.mainFont, self.game.assets.mainFont, self.game.assets.mainFont]
        fonts[selected] = self.game.assets.boldFont
        images = []
        for key in ["music", "sound"]:
            if settings[key]:
                images.append(self.game.assets.fullBox)
            else:
                images.append(self.game.assets.hollowBox)
        i = 0
        musicLabel = fonts[i].render(
            "Music", 1, self.defaultCol
        )
        i += 1
        soundLabel = fonts[i].render(
            "Sound", 1, self.defaultCol
        )
        i += 1
        backLabel = fonts[i].render(
            "Back", 1, self.defaultCol
        )
        i = 0
        y = self.height / 3
        self.window.blit(
            musicLabel, (self.width / 2 - musicLabel.get_width() / 2, y)
        )
        size = musicLabel.get_height() - 10
        self.window.blit(
            pygame.transform.scale(images[i], (size, size)),
            (self.width / 2 + musicLabel.get_width() / 2 + 40, y + 5)
        )
        i += 1
        y += musicLabel.get_height() * 3
        self.window.blit(
            soundLabel, (self.width / 2 - soundLabel.get_width() / 2, y)
        )
        size = soundLabel.get_height() - 10
        self.window.blit(
            pygame.transform.scale(images[i], (size, size)),
            (self.width / 2 + soundLabel.get_width() / 2 + 40, y + 5)
        )
        i += 1
        y += soundLabel.get_height() * 3
        self.window.blit(
            backLabel, (self.width / 2 - backLabel.get_width() / 2, y)
        )
        y += backLabel.get_height() * 3
        pygame.display.update()
        return

    def drawFrame(self):
        self.window.blit(self.game.assets.BackgroundImage, (0,0))
        scoreLabel = self.game.assets.mainFont.render(
            "Score: {}".format(self.game.score),
             1, self.defaultCol
        )
        timeLabel = self.game.assets.mainFont.render(
            "Time: %.2f" % self.game.timeAlive,
            1, self.defaultCol
        )
        fuelLabel = self.game.assets.mainFont.render(
            "Fuel: {}".format(self.game.player.fuel),
            1, self.defaultCol
        )
        maxSize = self.width - scoreLabel.get_width() - timeLabel.get_width() - 40 - 120
        fuelBar = pygame.transform.scale(
            self.game.assets.fullBox,
            (maxSize * (self.game.player.fuel / self.game.player.maxfuel),
            scoreLabel.get_height())
        )
        self.window.blit(scoreLabel, (20, 20))
        #self.window.blit(
        #    fuelLabel, (self.width/2 - fuelLabel.get_width()/2, 20)
        #)
        self.window.blit(
            fuelBar, (scoreLabel.get_width() + 80, 20)
        )
        self.window.blit(
            timeLabel, (self.width - timeLabel.get_width() - 20, 20)
        )
        for item in self.game.toDraw:
            self.window.blit(item.image, (item.x, item.y))
        pygame.display.update()

    def endScreen(self):
        gameOverText = self.game.assets.mainFont.render(
            "Game Over",
            1, self.defaultCol
        )
        continueText = self.game.assets.mainFont.render(
            "Press Enter",
            1, self.defaultCol
        )
        self.window.blit(
            gameOverText,
            (self.width/2 - gameOverText.get_width()/2,
            self.height / 3)
        )
        self.window.blit(
            continueText,
            (self.width/2 - continueText.get_width()/2,
            self.height / 3 + gameOverText.get_height() * 2)
        )
        pygame.display.update()
        return

    def enterName(self, playerName):
        timeText = self.game.assets.mainFont.render(
            "Survived: %.2f seconds" % self.game.timeAlive,
            1, self.defaultCol
        )
        scoreText = self.game.assets.mainFont.render(
            "Score: {}".format(self.game.score),
            1, self.defaultCol
        )
        highscoreText = self.game.assets.mainFont.render(
            "Highscore: {}".format(self.game.highscore),
            1, self.defaultCol
        )
        promptText = self.game.assets.mainFont.render(
            "Enter your name:",
            1,
            self.defaultCol
        )
        playerNameText = self.game.assets.mainFont.render(
            playerName,
            1,
            self.defaultCol
        )
        self.window.blit(self.game.assets.BackgroundImage, (0,0))
        self.window.blit(
            timeText,
            (self.width/2 - timeText.get_width()/2,
            self.height/3)
        )
        self.window.blit(
            scoreText,
            (self.width/2 - scoreText.get_width()/2,
            self.height/3 + timeText.get_height())
        )
        self.window.blit(
            highscoreText,
            (self.width/2 - highscoreText.get_width()/2,
            self.height/3 + timeText.get_height() + scoreText.get_height())
        )
        self.window.blit(
            promptText,
            (self.width/2 - promptText.get_width()/2,
            self.height/3 + timeText.get_height() + scoreText.get_height() + \
                highscoreText.get_height() * 2)
        )
        self.window.blit(
            playerNameText,
            (self.width/2 - playerNameText.get_width()/2,
            self.height/3 + timeText.get_height() + scoreText.get_height() + \
                + highscoreText.get_height() * 2 + promptText.get_height())
        )
        pygame.display.update()

    def recapScreen(self, timeAlive, playerName):
        self.window.blit(self.game.assets.BackgroundImage, (0,0))
        pygame.display.update()
