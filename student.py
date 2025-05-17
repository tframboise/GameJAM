'''
EPITECH PROJECT, 2025
Game JAM
File description:
student.py
'''

import pygame
import random
from settings import RED, PURPLE, WIDTH, HEIGHT

class Student(pygame.sprite.Sprite):
    def __init__(self, pos, player):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=pos)
        self.state = "calm"
        self.player = player
        self.time_to_go_crazy = pygame.time.get_ticks() + random.randint(3000, 10000)
        self.speed = 2.5

    def update(self):
        now = pygame.time.get_ticks()

        if self.state == "calm":
            if now >= self.time_to_go_crazy:
                self.go_crazy()

        elif self.state == "crazy":
            direction = pygame.Vector2(
                self.player.rect.centerx - self.rect.centerx,
                self.player.rect.centery - self.rect.centery
            )
            if direction.length() != 0:
                direction = direction.normalize()
                self.rect.x += direction.x * self.speed
                self.rect.y += direction.y * self.speed

            self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def go_crazy(self):
        self.state = "crazy"
        self.image.fill(PURPLE)
