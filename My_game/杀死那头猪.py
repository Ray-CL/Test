# -*- coding=utf-8 -*-
# Time:2022/10/4 23:12
# Author:Ray
# File:杀死那头猪.py
# Software:PyCharm
from my_game import *


def my_game():
    game = Init()
    screen = pygame.display.set_mode((game.length, game.width))
    ship = Ship(game, screen)
    pygame.display.set_caption("Kill Pigs")
    shot = Group()
    pig = Group()
    creat_pig(game, screen, pig)
    while True:
        ship.update()
        check_event(game, screen, ship, shot)
        update_screen(game, screen, ship, shot, pig)


if __name__ == "__main__":
    my_game()
