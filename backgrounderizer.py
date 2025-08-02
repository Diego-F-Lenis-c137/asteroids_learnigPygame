
import pygame
import math as m
import random as r

class Backgrounderizer():

    def __init__(self, resolution: tuple, screen):
        self.w = resolution[0]
        self.h = resolution[1]
        self.center = (resolution[0]//2, resolution[1]//2)
        self.n = 50

        self.angle       = 0.0
        self.angular_vel = 0.2
        self.stars = self.design()
        self.surf = pygame.Surface((self.w, self.h))
        self.screen = screen    

    def design(self):
        
        stars = []
        for x in range(self.n):
            
            ang = r.randint(0, 360)
            pos = ((2*x*(m.cos(ang))), (2*x*(m.sin(ang))))
            pos = (pos[0] + self.w//2, pos[1] + self.h//2)
            star = [pos, ang, x]
            stars.append(star)

        return stars
    
    def update(self, dt: float):
        self.surf.fill((0, 0, 0))

        for i in self.stars:

            ang = (i[1] + self.angular_vel * dt) % 360
            pos = ((20*i[2]*(m.cos(ang))), (20*i[2]*(m.sin(ang)))) 
            pos = (pos[0] + self.w//2, pos[1] + self.h//2)
            i[0] = (pos) 
            i[1] = (ang)

    def draw(self, dt: float):
        self.update(dt)
        for i in self.stars:
            pygame.draw.rect(self.surf, (255,255,255), (i[0][0], i[0][1], 1, 1))
        self.screen.blit(self.surf, (0, 0, self.w, self.h))