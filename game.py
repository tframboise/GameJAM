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

        for _ in range(30):
            pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
            student = Student(pos, self.player)
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
        self.students.update()

        for student in self.students:
            if student.state == "crazy":
                for other in self.students:
                    if other != student and other.rect.colliderect(student.rect):
                        dx = student.rect.centerx - other.rect.centerx
                        dy = student.rect.centery - other.rect.centery
                        move = pygame.Vector2(dx, dy)
                        if move.length() != 0:
                            move = move.normalize() * 1
                            student.rect.move_ip(move)


    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
