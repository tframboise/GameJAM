'''
EPITECH PROJECT, 2025
Game JAM
File description:
game.py
'''

import pygame
import sys
import random
from settings import WIDTH, HEIGHT, FPS
from player import Player
from student import Student
from gem import MagicGemDrop, MagicGemUI

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maîtresse en Détresse")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.students = pygame.sprite.Group()
        self.player = Player((WIDTH // 2, HEIGHT // 2))
        self.all_sprites.add(self.player)
        self.gem_drops = pygame.sprite.Group()
        self.gem_ui = MagicGemUI()
        self.collected_gems = 0
        self.next_gem_spawn = pygame.time.get_ticks() + 5000

        for _ in range(5):
            pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
            student = Student(pos, self.player)
            self.students.add(student)
            self.all_sprites.add(student)
        self.background = pygame.image.load("assets/classroom.png").convert()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.collected_gems > 0:
                        for student in self.students:
                            if student.state == "crazy" and student.rect.collidepoint(mouse_pos):
                                student.calm_down()
                                self.collected_gems -= 1
                                break
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

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
                            move = move.normalize()
                            student.rect.move_ip(move)
        now = pygame.time.get_ticks()
        if now >= self.next_gem_spawn:
            pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
            gem = MagicGemDrop(pos)
            self.gem_drops.add(gem)
            self.next_gem_spawn = now + random.randint(7000, 12000)
        for gem in self.gem_drops:
            if self.player.rect.colliderect(gem.rect):
                self.collected_gems += 1
                self.gem_drops.remove(gem)


    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.gem_drops.draw(self.screen)
        self.gem_ui.draw(self.screen, self.collected_gems)
        pygame.display.flip()
