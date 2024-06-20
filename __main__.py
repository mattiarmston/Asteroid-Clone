#!/usr/bin/env python3

import argparse
import json
import pygame

from game import Game

def parseArgs():
    parser = argparse.ArgumentParser(
        description='Process command line arguments')
    parser.add_argument(
        '--version',
        action='store_true',
        help='output version information and exit'
    )
    return parser.parse_args()

def main():
    pygame.init()
    args = parseArgs()
    loadGame(args)

def loadHighscores():
    try:
        with open("highscores.json", 'r') as file:
            scores = json.load(file)
    except Exception:
        scores = []
        print("Error cannot load highscores")
    return scores

def loadGame(args):
    def player():
        scores = loadHighscores()
        game = Game(scores)
        game.titleScreen()

    def version():
        print("Version {}".format('0.5.0'))
        print("This project is still in active development")
        print("Visit https://github.com/mattiarmston/asteroid-clone for the latest version")

    if args.version:
        version()
        quit()
    else:
        player()

if __name__ == "__main__":
    main()
