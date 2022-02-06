#!/usr/bin/env python3

import pygame
import argparse

from game import Game

def parseArgs():
    parser = argparse.ArgumentParser(description='Process command line arguments')
    parser.add_argument('--version', action='store_true', help='output version information and exit')
    parser.add_argument('--ai', action='store_true', help='uses neat to train ai to play')
    return parser.parse_args()

def main():
    pygame.init()
    args = parseArgs()
    loadGame(args)

def loadGame(args):
    def player():
        game = Game()
        game.mainMenu()

    def ai():
        import neat
        startNeat()

    def version():
        print("Version {}".format('0.3.0'))
        print("This project is still in active development")
        print("Visit https://github.com/crus4d3/asteroid-clone for the latest version")

    if args.version:
        version()
        quit()
    if args.ai:
        ai()
    else:
        player()

def startNeat():
    config = neat.config.Config(
        neat.genome.DefaultGenome,
        neat.reproduction.DefaultReproduction,
        neat.species.DefaultSpeciesSet,
        neat.stagnation.DefaultStagnation,
        'neatConfig.txt'
    )
    population = neat.population.Population(config)
    population.run(eval_genomes, 50)

if __name__ == "__main__":
    main()
