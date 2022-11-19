# -*- coding=utf-8 -*-
# Time:2022/10/4 21:50
# Author:Ray
# File:my_game.py
# Software:PyCharm
import time

import pygame
import sys

from pygame.sprite import *


class Init:
    def __init__(self):
        """战机"""
        self.length = 900
        self.width = 800
        self.color = (230, 230, 230)
        self.speed = 0.45
        self.ship_limit = 3
        """子弹"""
        self.shot_speed = 0.6
        self.shot_length = 3
        self.shot_width = 15
        self.shot_color = (60, 60, 60)
        """猪"""
        self.pig_speed =0.1
        self.pig_length = 100
        self.none = (0, 0, 0)


class State:

    def __init__(self, game):
        self.game = game
        self.reset()

    def reset(self):
        self.ships_left = self.game.ship_limit


"""初始化飞船"""


class Ship:
    def __init__(self, game, screen):
        self.screen = screen
        self.image = pygame.image.load("images/2.bmp")
        self.image = pygame.transform.scale(self.image, (80, 60))  # 修改图片尺寸
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        """"发射物体居中"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

        self.game = game
        self.center = float(self.rect.centerx)

    def draw_image(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.game.speed
        if self.move_left and self.rect.left > 0:
            self.center -= self.game.speed
        self.rect.centerx = self.center

    def game_over(self, screen):
        self.screen = screen
        self.image = pygame.image.load("images/gameover.bmp")
        self.image = pygame.transform.scale(self.image, (400, 300))  # 修改图片尺寸
        self.rect = self.image.get_rect()
        self.rect.y=300
        screen.blit(self.image, self.rect)


class Shot(Sprite):
    def __init__(self, game, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, game.shot_length, game.shot_width)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.top)
        self.color = game.shot_color
        self.speed = game.shot_speed

    def update(self, game, screen, shot, pig):
        self.y -= self.speed
        self.rect.y = self.y
        dict = pygame.sprite.groupcollide(shot, pig, True, True)
        if (len(pig) == 0):
            creat_pig(game, screen, pig)

    def draw_shot(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Pig(Sprite):
    def __init__(self, game, screen):
        super().__init__()
        self.screen = screen
        self.game = game
        self.image = pygame.image.load('images/4.bmp')
        self.image = pygame.transform.scale(self.image, (80,60))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = game.pig_speed
        self.color = (60, 60, 60)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw_image(self):
        self.screen.blit(self.image, self.rect)


def creat_pig(game, screen, pig):
    a_length = game.length
    num = int((a_length - game.pig_length) / 2 / game.pig_length)
    row = 2
    for i in range(row):
        for n in range(num):
            a = Pig(game, screen)
            a.rect.y = 90 * i
            a.rect.x = (2 * n + 1) * game.pig_length
            pig.add(a)


def check_event(game, screen, ship, shot):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down(event, game, screen, ship, shot)
        elif event.type == pygame.KEYUP:
            key_up(ship, event)


def key_down(event, game, screen, ship, shot):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        new_shot = Shot(game, screen, ship)
        shot.add(new_shot)
    elif event.key == pygame.K_q:
        sys.exit()


def key_up(ship, event):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    if event.key == pygame.K_LEFT:
        ship.move_left = False


"""更新屏幕"""


def update_screen(game, screen, ship, shot, pig):
    screen.fill(game.color)
    ship.draw_image()
    for temp in pig.sprites():
        if temp.rect.y == game.width:
            ship.game_over(screen)
        temp.draw_image()
        temp.update()
    """子弹"""
    for temp in shot.sprites():
        temp.update(game, screen, shot, pig)
        temp.draw_shot()
    for s in shot.copy():
        if s.rect.top <= 0:
            shot.remove(s)
    if pygame.sprite.spritecollideany(ship, pig):
        ship.game_over(screen)

    pygame.display.flip()
