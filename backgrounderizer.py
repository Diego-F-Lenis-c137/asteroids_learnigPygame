import pygame
import random as r

class Backgrounderizer():




# ...existing code...
    def __init__(self, resolution: tuple, screen):
        self.w = resolution[0]
        self.h = resolution[1]
        self.side = max(self.w, self.h)
        self.center = (self.w//2, self.h//2)
        self.corners = ((0,0), (self.w,0), (0, self.h), (self.w, self.h))

        self.angle       = 0.0
        self.angular_vel = 36
        self.orig_image = self.design()
        self.image = self.orig_image
        self.screen = screen
        

    def design(self):
        surf = pygame.Surface((self.side,self.side),pygame.SRCALPHA)
        s = self.side//4
        for x in range(s):
            n = (r.randint(0, s)*4, r.randint(0, s)*4)
            pygame.draw.line(surf, (255,255,255), n, n, 1)
        return surf
    
    def draw(self, dt: float):
        self.screen.blit(self.image, self.image.get_rect(center = self.center))

'''
import pygame
import random as r

class Backgrounderizer():




# ...existing code...
    def __init__(self, resolution: tuple, screen):
        self.w = resolution[0]
        self.h = resolution[1]
        self.side = max(self.w, self.h)
        self.center = (self.w//2, self.h//2)
        self.corners = ((0,0), (self.w,0), (0, self.h), (self.w, self.h))

        self.angle       = 0.0
        self.angular_vel = 36
        self.orig_image = self.design()
        self.image = self.orig_image
        self.screen = screen
        self.cache_steps = 36  # 10-degree steps
        self.rotation_cache = [
            pygame.transform.rotate(self.orig_image, angle)
            for angle in range(0, 360, 360 // self.cache_steps)
        ]

    def design(self):
        surf = pygame.Surface((self.side,self.side),pygame.SRCALPHA)
        #pygame.draw.line(self.surf, (0, 100, 100), self.corners[0], self.corners[3], 2) 
        #pygame.draw.line(self.surf, (0, 100, 100), self.corners[1], self.corners[2], 2)
        #pygame.draw.rect(self.surf, (0,0,0), (self.w//4, self.h//4, self.w//2, self.h//2), 0)
        #pygame.draw.rect(self.surf, (0,100,100), (self.w//4, self.h//4, self.w//2, self.h//2), 2)
        s = self.side//4
        for x in range(s):
            n = (r.randint(0, s)*4, r.randint(0, s)*4)
            pygame.draw.line(surf, (255,255,255), n, n, 1)
        return surf
    
    def draw(self, dt: float):
        self.angle = (self.angle + self.angular_vel * dt) % 360
        idx = int(self.angle / 360 * self.cache_steps) % self.cache_steps
        rotated = self.rotation_cache[idx]
        rotated_rect = rotated.get_rect(center=self.center)
        screen_rect = pygame.Rect(0, 0, self.w, self.h)
        cropped_surface = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        cropped_surface.blit(rotated, (rotated_rect.topleft[0] - screen_rect.topleft[0], rotated_rect.topleft[1] - screen_rect.topleft[1]))
        self.screen.blit(cropped_surface, (0, 0))
'''