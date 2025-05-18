'''
EPITECH PROJECT, 2025
Game JAM
File description:
student.py
'''

import pygame
import random
from settings import WIDTH, HEIGHT

class Student(pygame.sprite.Sprite):
    def __init__(self, pos, player, game, chair_pos):
        super().__init__()
        self.player = player
        self.game = game
        self.state = "calm"
        self.speed = 1.8
        self.chair_pos = pygame.Vector2(chair_pos)

        self.calm_sheet = pygame.image.load("assets/students.png").convert_alpha()
        self.crazy_sheet = pygame.image.load("assets/crazy_students.png").convert_alpha()
        self.frame_width = self.calm_sheet.get_width() // 4
        self.frame_height = self.calm_sheet.get_height() // 4
        self.scale = 2
        self.animations = {
            "calm": self.load_frames(self.calm_sheet),
            "crazy": self.load_frames(self.crazy_sheet)
        }

        self.direction = "down"
        self.frame = 0
        self.timer = 0
        self.animation_speed = 0.15
        self.image = self.animations[self.state][self.direction][self.frame]
        self.rect = self.image.get_rect(center=pos)
        self.time_to_go_crazy = pygame.time.get_ticks() + random.randint(3000, 10000)

    def load_frames(self, sheet):
        frames_by_direction = {}
        directions = ["down", "left", "right", "up"]
        for i, dir in enumerate(directions):
            frames = []
            for j in range(4):
                x = j * self.frame_width
                y = i * self.frame_height
                frame = sheet.subsurface(pygame.Rect(x, y, self.frame_width, self.frame_height))
                frame = pygame.transform.scale(frame, (self.frame_width * self.scale, self.frame_height * self.scale))
                frames.append(frame)
            frames_by_direction[dir] = frames
        return frames_by_direction

    def update(self):
        now = pygame.time.get_ticks()

        if self.state == "calm":
            if now >= self.time_to_go_crazy:
                self.go_crazy()
            else:
                direction_vector = self.chair_pos - pygame.Vector2(self.rect.center)
                if direction_vector.length() > 1:
                    direction_vector = direction_vector.normalize()
                    self.rect.x += direction_vector.x * self.speed
                    self.rect.y += direction_vector.y * self.speed

        elif self.state == "crazy":
            direction_vector = pygame.Vector2(
                self.player.rect.centerx - self.rect.centerx,
                self.player.rect.centery - self.rect.centery
            )
            if direction_vector.length() != 0:
                direction_vector = direction_vector.normalize()
                self.rect.x += direction_vector.x * self.speed
                self.rect.y += direction_vector.y * self.speed

            if abs(direction_vector.x) > abs(direction_vector.y):
                self.direction = "right" if direction_vector.x > 0 else "left"
            else:
                self.direction = "down" if direction_vector.y > 0 else "up"

            self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

        self.timer += self.animation_speed
        if self.timer >= len(self.animations[self.state][self.direction]):
            self.timer = 0
        self.frame = int(self.timer)
        self.image = self.animations[self.state][self.direction][self.frame]

    def go_crazy(self):
        self.state = "crazy"

    def calm_down(self):
        self.state = "calm"
        self.time_to_go_crazy = pygame.time.get_ticks() + random.randint(6000, 12000)
