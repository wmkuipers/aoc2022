#!/usr/bin/env python

from aocd import get_data, submit
import os

from games import RockPaperScissors, part_two

def parseGames(gamesdata):
    games = []
    for game_data in gamesdata.split("\n"):
        games.append(RockPaperScissors(game_data))

    print(f"Part one: {sum([game.score for game in games])}")

    p2 = [part_two[game.user_plays][game.elf_plays] for game in games]
    print(p2)
    print(sum(p2))
    # submit(sum(p2))



def main(test=False):
    if test:
        raw_data = open("test.txt").read()
    else:
        day = int(os.getcwd()[-2:])
        raw_data = get_data(day=day, year=2022)
    
    parseGames(raw_data)

if __name__ == '__main__':
    main()