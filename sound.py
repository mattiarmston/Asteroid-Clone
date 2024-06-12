import pathlib
import pygame

class Sound():
    def __init__(self, game):
        self.sound = pathlib.Path("sound/")
        self.game = game

    def playMainLoop(self):
        if not self.game.playerSettings["music"]:
            pygame.mixer.music.stop()
            return
        pygame.mixer.music.load(self.sound / "tavern_loop2_2.mp3")
        pygame.mixer.music.play(-1)

    def updateSettings(self):
        self.playMainLoop()
