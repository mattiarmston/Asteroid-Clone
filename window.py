import pygame

class Window():
    def __init__(self, game):
        self.game = game
        self.width, self.height = 1000, 1000
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Asteroid clone")

    def mainMenu(self, selected):
        playCol = (150, 150, 150)
        helpCol = (150, 150, 150)
        if selected == 0:
            playCol = (255, 255, 255)
        elif selected == 1:
            helpCol = (255, 255, 255)
        playText = self.game.assets.mainFont.render(
            'Play',
            1, playCol
        )
        helpText = self.game.assets.mainFont.render(
            'Help',
            1, helpCol
        )
        self.window.blit(self.game.assets.BackgroundImage, (0,0))
        self.window.blit(
            playText,
            (self.width / 2 - playText.get_width() / 2,
            self.height / 3)
        )
        self.window.blit(
            helpText,
            (self.width / 2 - helpText.get_width() / 2,
            self.height / 2 + helpText.get_height() / 2)
        )
        pygame.display.update()

    def help(self):
        controlsText = self.game.assets.mainFont.render(
            "Use WASD or Arrow Keys to move.",
            1, (150, 150, 150)
        )
        objectiveText = self.game.assets.mainFont.render(
            "Collect yellow Coins and",
            1, (150, 150, 150)
        )
        objectiveText2 = self.game.assets.mainFont.render(
            "avoid grey Asteriods",
            1, (150, 150, 150)
        )
        backText = self.game.assets.mainFont.render(
            "Press Enter to go back",
            1, (150, 150, 150)
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

    def drawFrame(self):
        self.window.blit(self.game.assets.BackgroundImage, (0,0))
        for item in self.game.toDraw:
            self.window.blit(item.image, (item.x, item.y))
        scoreLabel = self.game.assets.mainFont.render(
            "Score: {}".format(self.game.score),
             1, (150, 150, 150)
        )
        timeLabel = self.game.assets.mainFont.render(
            "Time: %.2f" % self.game.timeAlive,
            1, (150, 150, 150)
        )
        self.window.blit(scoreLabel, (20, 20))
        self.window.blit(timeLabel, (self.width - timeLabel.get_width() - 20, 20))
        pygame.display.update()

    def endScreen(self):
        gameOverText = self.game.assets.mainFont.render(
            "Game Over",
            1, (150, 150, 150)
        )
        continueText = self.game.assets.mainFont.render(
            "Press Enter",
            1, (150, 150, 150)
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
            1, (150, 150, 150)
        )
        scoreText = self.game.assets.mainFont.render(
            "Score: {}".format(self.game.score),
            1, (150, 150, 150)
        )
        highscoreText = self.game.assets.mainFont.render(
            "Highscore: {}".format(self.game.highscore),
            1, (150, 150, 150)
        )
        promptText = self.game.assets.mainFont.render(
            "Enter your name:",
            1,
            (150, 150, 150)
        )
        playerNameText = self.game.assets.mainFont.render(
            playerName,
            1,
            (150, 150, 150)
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
