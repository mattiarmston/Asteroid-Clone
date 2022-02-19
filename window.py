import pygame

class Window():
    def __init__(self, game):
        self.game = game
        self.width, self.height = 1000, 1000
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Asteroid clone")

    def drawFrame(self):
        self.window.blit(self.game.assets.BackgroundImage, (0,0))
        for item in self.game.toDraw:
            self.window.blit(item.image, (item.x, item.y))
        scoreLabel = self.game.mainFont.render(
            "Score: {}".format(self.game.score),
             1, (150, 150, 150)
        )
        timeLabel = self.game.mainFont.render(
            "Time: %.2f" % self.game.timeAlive,
            1, (150, 150, 150)
        )
        self.window.blit(scoreLabel, (20, 20))
        self.window.blit(timeLabel, (self.width - timeLabel.get_width() - 20, 20))
        pygame.display.update()

    def menuScreen(self):
        self.window.blit(self.game.assets.BackgroundImage, (0,0))
        self.promptText = self.game.mainFont.render(
            "Enter your name:",
            1,
            (150, 150, 150)
        )
        nameText = self.game.mainFont.render(
            self.game.name,
            1,
            (150, 150, 150)
        )
        continueText = self.game.mainFont.render(
             "Press enter to play",
             1,
             (150, 150, 150)
        )
        self.window.blit(
            self.promptText,
            (self.width/2 - self.promptText.get_width()/2,
            self.height/2.25)
        )
        self.window.blit(
            nameText,
            (self.width/2 - nameText.get_width()/2,
            self.height/2.25+ self.promptText.get_height())
        )
        self.window.blit(
            continueText,
            (self.width/2 - continueText.get_width()/2,
            self.height/2.25+ self.promptText.get_height() + self.promptText.get_height())
        )
        pygame.display.update()

    def endScreen(self, timeAlive, playerName):
        bufferheight = 5
        playerNameText = self.game.mainFont.render(
            "Player: {}".format(playerName),
            1, (150, 150, 150)
        )
        timeText = self.game.mainFont.render(
            "Survived: %.2f seconds" % self.game.timeAlive,
            1, (150, 150, 150)
        )
        longestTimeText = self.game.mainFont.render(
            "Longest time: %.2f seconds" % self.game.longestTime,
            1, (150, 150, 150)
        )
        scoreText = self.game.mainFont.render(
            "Score: {}".format(self.game.score),
            1, (150, 150, 150)
        )
        highscoreText = self.game.mainFont.render(
            "Highscore: {}".format(self.game.highscore),
            1, (150, 150, 150)
        )
        self.window.blit(
            playerNameText,
            (self.width/2 - playerNameText.get_width()/2,
            self.height/2.25)
        )
        self.window.blit(
            scoreText,
            (self.width/2 - scoreText.get_width()/2,
            self.height/2.25 + playerNameText.get_height())
        )
        self.window.blit(
            highscoreText,
            (self.width/2 - highscoreText.get_width()/2,
            self.height/2.25 + playerNameText.get_height() + scoreText.get_height())
        )
        self.window.blit(
            timeText,
            (self.width/2 - timeText.get_width()/2,
            self.height/2.25 + highscoreText.get_height() + scoreText.get_height() + playerNameText.get_height())
        )
        pygame.display.update()
