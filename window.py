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
        startText = self.game.mainFont.render("Press enter to play", 1, (150, 150, 150))
        self.window.blit(
            startText,
            (self.width/2 - startText.get_width()/2,
            self.height/2 - startText.get_height()/2)
        )
        pygame.display.update()

    def endScreen(self, timeAlive):
        bufferheight = 5
        timeText = self.game.mainFont.render(
            "You survived for %.2f seconds" % self.game.timeAlive,
            1, (150, 150, 150)
        )
        scoreText = self.game.mainFont.render(
            "Your score is {}".format(self.game.score),
            1, (150, 150, 150)
        )
        highscoreText = self.game.mainFont.render(
            "Your highscore is {}".format(self.game.highscore),
            1, (150, 150, 150)
        )
        self.window.blit(
            scoreText,
            (self.width/2 - scoreText.get_width()/2,
            self.height/2 - scoreText.get_height()/2)
        )
        self.window.blit(
            highscoreText,
            (self.width/2 - highscoreText.get_width()/2,
            self.height/2 + highscoreText.get_height()/2 + bufferheight)
        )
        self.window.blit(
            timeText,
            (self.width/2 - timeText.get_width()/2,
            self.height/2 - scoreText.get_height() - timeText.get_height()/2 - bufferheight)
        )
        pygame.display.update()
