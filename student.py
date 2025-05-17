'''
EPITECH PROJECT, 2025
Game JAM
File description:
student.py
'''

import pygame
from settings import RED

class Student(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=pos)
        self.state = "calm"
