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
            pos = ((20*x*(m.cos(ang))), (20*x*(m.sin(ang))))
            pos = (pos[0] + self.w//2, pos[1] + self.h//2)
            # Precompute color
            r_val = abs(int(pos[0]) // 10)
            g_val = abs(int(pos[1]) // 10)
            b_val = (r_val + g_val) // 2
            color = (r_val, g_val, b_val)
            star = [pos, ang, x, color]
            
            stars.append(star)
        return stars

    def update(self, dt: float):
        self.surf.fill((0, 0, 0))
        for i in self.stars:
            ang = (i[1] + self.angular_vel * dt) % 360
            pos = ((20*i[2]*(m.cos(ang))), (20*i[2]*(m.sin(ang))))
            pos = (pos[0] + self.w//2, pos[1] + self.h//2)
            i[0] = pos
            i[1] = ang
            # Recalculate color based on new position
            
            r_val = abs(int(pos[0]) // 10) + 50
            g_val = abs(int(pos[1]) // 10) + 50
            b_val = ((r_val + g_val) // 2) + 50
            if r_val > 255: r_val = 255
            if g_val > 255: g_val = 255
            if b_val > 255: b_val = 255
            i[3] = (r_val, g_val, b_val)

    def draw(self, dt: float):
        self.update(dt)
        for i in self.stars:
            x, y = int(i[0][0]), int(i[0][1])
            color = i[3] # index 3 for polar coordinates version
            color = r.choices([color, (255, 255, 255), (0,0,0)], weights=[0.8, 0.1, 0.01], k=1)[0]
            pygame.draw.rect(self.surf, color, (x, y, 3, 3))
        self.screen.blit(self.surf, (0, 0, self.w, self.h))
