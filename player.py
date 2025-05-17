'''
EPITECH PROJECT, 2025
Game JAM
File description:
player.py
'''

import pygame
from settings import WIDTH, HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.spritesheet = pygame.image.load("assets/teacher.png").convert_alpha()
        self.frame_width = self.spritesheet.get_width() // 4
        self.frame_height = self.spritesheet.get_height() // 4

        self.animations = self.load_frames()
        self.direction = "down"
        self.frame = 0
        self.animation_speed = 0.15
        self.image = self.animations[self.direction][self.frame]
        self.rect = self.image.get_rect(center=pos)

        self.speed = 3
        self.timer = 0

    def load_frames(self):
        direction_indices = {
            "down": 0,
            "left": 1,
            "right": 2,
            "up": 3
        }
        scale = 2
        animations = {}
        for direction, i in direction_indices.items():
            frames = []
            for j in range(4):
                x = j * self.frame_width
                y = i * self.frame_height
                frame = self.spritesheet.subsurface(pygame.Rect(x, y, self.frame_width, self.frame_height))
                zoomed = pygame.transform.scale(frame, (self.frame_width * scale, self.frame_height * scale))
                frames.append(zoomed)
            animations[direction] = frames
        return animations

    def update(self, keys):
        dx = dy = 0
        prev_direction = self.direction

        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            dx = -self.speed
            self.direction = "left"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = self.speed
            self.direction = "right"
        elif keys[pygame.K_UP] or keys[pygame.K_z]:
            dy = -self.speed
            self.direction = "up"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = self.speed
            self.direction = "down"

        self.rect.x += dx
        self.rect.y += dy
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

        moving = dx != 0 or dy != 0
        if moving:
            self.timer += self.animation_speed
            if self.timer >= len(self.animations[self.direction]):
                self.timer = 0
            self.frame = int(self.timer)
        else:
            self.frame = 0
            self.timer = 0

        self.image = self.animations[self.direction][self.frame]
