#!/usr/bin/env python3

import pygame
import neat
from game import Game

def main():
    pygame.init()
    game = Game()
    game.mainMenu()

if __name__ == "__main__":
    main()
