import pathlib
import pygame

class Sound():
    def __init__(self, game):
        self.sound = pathlib.Path("sound/")
        # Occasionally when starting the game, the shell outputs:
        # `ALSA lib pcm.c:8740:(snd_pcm_recover) underrun occurred`
        # continuously till game closes. A faint clicking sound can
        # also be heard in the audio. I should find a fix for this.
        #pygame.mixer.pre_init(buffer=2048)
        self.musicChannel = pygame.mixer.Channel(1)
        self.sfxChannel = pygame.mixer.Channel(2)
        self.mainLoop = pygame.mixer.Sound(self.sound / "mainLoop.ogg")
        self.explosion = pygame.mixer.Sound(self.sound / "explosion.ogg")
        self.fizzle = pygame.mixer.Sound(self.sound / "fizzle.ogg")
        self.fuelCollect = pygame.mixer.Sound(self.sound / "fuelCollect.ogg")
        self.game = game

    def playMainLoop(self):
        if not self.musicChannel.get_busy():
            self.musicChannel.play(self.mainLoop, loops=-1)
        if not self.game.playerSettings["music"]:
            self.musicChannel.set_volume(0)
        else:
            self.musicChannel.set_volume(1)

    # There is a better way of doing this, but I think it should be fine for now.
    def playExplosion(self):
        if not self.game.playerSettings["sound"]:
            return
        self.sfxChannel.play(self.explosion)
        return

    def playFizzle(self):
        if not self.game.playerSettings["sound"]:
            return
        self.sfxChannel.play(self.fizzle)
        return

    def playFuelCollect(self):
        if not self.game.playerSettings["sound"]:
            return
        self.sfxChannel.play(self.fuelCollect)
        return

    def updateSettings(self):
        self.playMainLoop()
