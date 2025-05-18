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
        pygame.display.set_caption("Mistress in Distress")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.students = pygame.sprite.Group()
        self.player = Player((WIDTH // 2, HEIGHT // 2))
        self.all_sprites.add(self.player)
        self.gem_drops = pygame.sprite.Group()
        self.gem_ui = MagicGemUI()
        self.collected_gems = 0
        self.next_gem_spawn = pygame.time.get_ticks() + 5000
        self.game_over = False
        self.victory = False
        self.chair_positions = [
            (115, 170), (210, 170),
            (115, 270), (210, 270),
            (115, 370), (210, 370),
            (115, 470), (210, 470),
            (1170, 170), (1070, 170),
        ]
        random.shuffle(self.chair_positions)

        for i in range(5):
            chair_pos = self.chair_positions[i]
            student = Student(chair_pos, self.player, self, chair_pos)
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
        for student in self.students:
            if student.state == "crazy" and student.rect.colliderect(self.player.rect):
                self.victory = False
                self.game_over = True
        if pygame.time.get_ticks() < 5000:
            return
        if all(student.state == "calm" for student in self.students):
            self.victory = True
            self.game_over = True

    def draw(self):
        if self.game_over:
            self.screen.fill((30, 30, 30) if not self.victory else (0, 100, 0))
            font = pygame.font.SysFont(None, 80)
            if self.victory:
                text = font.render("Victory! All the students are calm", True, (255, 255, 255))
            else:
                text = font.render("Defeat! A student touched you", True, (255, 0, 0))
            rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.screen.blit(text, rect)
        else:
            self.screen.blit(self.background, (0, 0))
            self.all_sprites.draw(self.screen)
            self.gem_drops.draw(self.screen)
            self.gem_ui.draw(self.screen, self.collected_gems)
        pygame.display.flip()
        if self.game_over:
            pygame.time.wait(4000)
            pygame.quit()
            sys.exit()
