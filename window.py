import pygame

class Window():
    def __init__(self, game):
        self.game = game
        self.width, self.height = 1000, 1000
        self.window = pygame.display.set_mode((self.width, self.height))
        self.FPS = 60
        self.frame = 0
        self.defaultCol = (255, 255, 255)
        pygame.display.set_caption("Asteroid clone")

    def titleScreen(self):
        titleText = self.game.assets.titleFont.render(
            "Asteroid Clone", 1, self.defaultCol
        )
        enterText = self.game.assets.mainFont.render(
            "Press Enter", 1, self.defaultCol
        )
        self.window.blit(self.game.assets.BackgroundImage, (0,0))
        y = self.height / 2
        y -= titleText.get_height()
        self.window.blit(
            titleText, (self.width / 2 - titleText.get_width() / 2, y)
        )
        y += titleText.get_height()
        y += enterText.get_height()
        self.window.blit(
            enterText, (self.width / 2 - enterText.get_width() / 2, y)
        )
        y += enterText.get_height()
        pygame.display.update()
        return

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
            "Avoid Asteroids and collect fuel,",
            1, self.defaultCol
        )
        objectiveText2 = self.game.assets.mainFont.render(
            "to survive as long as possible.",
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
        self.window.blit(self.game.assets.BackgroundImage, (0,0))
        nameText = self.game.assets.mainFont.render(
            "Name", 1, self.defaultCol
        )
        timeText = self.game.assets.mainFont.render(
            "Time", 1, self.defaultCol
        )
        scoreText = self.game.assets.mainFont.render(
            "Score", 1, self.defaultCol
        )
        x = 30
        y = 30
        nameX = x + self.game.assets.mainFont.render(
            "15. ", 1, self.defaultCol).get_width()
        timeX = self.width - (200 + 30) * 2
        scoreX = self.width - (200 + 30)
        buffer = self.game.assets.mainFont.render("15. ", 1, self.defaultCol).get_width()
        self.window.blit(nameText, (nameX, y))
        self.window.blit(timeText, (timeX, y))
        self.window.blit(scoreText, (scoreX, y))
        y += nameText.get_height() + 10
        i = 1
        for score in scores:
            number = self.game.assets.mainFont.render(
                "{}. ".format(i), 1, self.defaultCol
            )
            name = self.game.assets.mainFont.render(
                "{}".format(score[0][0:14]), 1, self.defaultCol
            )
            time = self.game.assets.mainFont.render(
                "{time:.2f}".format(time=score[1]), 1, self.defaultCol
            )
            score = self.game.assets.mainFont.render(
                "{}".format(score[2]), 1, self.defaultCol
            )
            #name=score[0][0:14], num=i, time=score[1], score=score[2]),
            self.window.blit(number, (x,y))
            self.window.blit(name, (nameX, y))
            self.window.blit(time, (timeX, y))
            self.window.blit(score, (scoreX, y))
            y += name.get_height()
            i += 1
        backText = self.game.assets.boldFont.render(
            "Back",
            1, self.defaultCol
        )
        self.window.blit(
            backText, (self.width/2 - backText.get_width()/2, y + 30))
        pygame.display.update()
        return

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
        musicText = fonts[i].render(
            "Music", 1, self.defaultCol
        )
        i += 1
        soundText = fonts[i].render(
            "Sound", 1, self.defaultCol
        )
        i += 1
        backText = fonts[i].render(
            "Back", 1, self.defaultCol
        )
        i = 0
        y = self.height / 3
        self.window.blit(
            musicText, (self.width / 2 - musicText.get_width() / 2, y)
        )
        size = musicText.get_height() - 10
        self.window.blit(
            pygame.transform.scale(images[i], (size, size)),
            (self.width / 2 + musicText.get_width() / 2 + 40, y + 5)
        )
        i += 1
        y += musicText.get_height() * 3
        self.window.blit(
            soundText, (self.width / 2 - soundText.get_width() / 2, y)
        )
        size = soundText.get_height() - 10
        self.window.blit(
            pygame.transform.scale(images[i], (size, size)),
            (self.width / 2 + soundText.get_width() / 2 + 40, y + 5)
        )
        i += 1
        y += soundText.get_height() * 3
        self.window.blit(
            backText, (self.width / 2 - backText.get_width() / 2, y)
        )
        y += backText.get_height() * 3
        pygame.display.update()
        return

    def drawFrame(self, timeAlive):
        self.window.blit(self.game.assets.BackgroundImage, (0,0))
        scoreLabel = self.game.assets.mainFont.render(
            "Score: {}".format(self.game.score),
             1, self.defaultCol
        )
        #timeLabel = self.game.assets.mainFont.render(
        #    "Time: %.2f" % self.game.timeAlive,
        #    1, self.defaultCol
        #)
        timeLabel1 = self.game.assets.mainFont.render(
            "Time: ", 1, self.defaultCol
        )
        timeLabel2 = self.game.assets.mainFont.render(
            "{time:.2f}".format(time=timeAlive), 1, self.defaultCol
        )
        x = 20
        y = 10
        # Generally max width of numbers is 101px
        time2X = self.width - x - 101
        time1X = time2X - timeLabel1.get_width()
        buffer = 100
        maxSize = self.width - x - (self.width - time1X) - \
            scoreLabel.get_width() - buffer * 2
        fuelBar = pygame.transform.scale(
            self.game.assets.fullBox,
            (maxSize * (self.game.player.fuel / self.game.player.maxfuel),
            scoreLabel.get_height())
        )
        self.window.blit(scoreLabel, (x, y))
        x += scoreLabel.get_width()
        x += buffer
        self.window.blit(
            fuelBar, (x, y)
        )
        self.window.blit(
            timeLabel2, (time2X, y)
        )
        self.window.blit(
            timeLabel1, (time1X, y)
        )
        for item in self.game.toDraw:
            self.window.blit(item.image, (item.x, item.y))
        pygame.display.update()

    def endScreen(self):
        gameOverText = self.game.assets.mainFont.render(
            "Game Over",
            1, self.defaultCol
        )
        continueText = self.game.assets.boldFont.render(
            "Continue",
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
