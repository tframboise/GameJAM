'''
EPITECH PROJECT, 2025
Game JAM
File description:
game.py
'''

import pygame
import random
from settings import *
from player import Player
from student import Student

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maîtresse en Détresse")
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group()
        self.students = pygame.sprite.Group()

        self.background = pygame.image.load("assets/classroom.png").convert()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        self.player = Player(pos=(WIDTH // 2, HEIGHT // 2))
        self.all_sprites.add(self.player)

        for _ in range(5):
            pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
            student = Student(pos)
            self.students.add(student)
            self.all_sprites.add(student)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
