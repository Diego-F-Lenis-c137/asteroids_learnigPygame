# ship.py
import pygame
import math as m
import random as r
import infiniteparalax as paralax

class Asteroid(pygame.sprite.Sprite):

    def __init__(self, w, h, acceleration = 1.0, angular_vel=30.0):
        super().__init__()
        self._orig_image = self._build_asteroid_surface()  # cache the artwork
        self.image       = self._orig_image          # what gets blitted
        self.position = r.choice([[r.randint(10, (w//2)-250), r.randint(10, (h//2)-250)], [r.randint((w//2)+250, w-10), r.randint((h//2)-250, h-10)],
                                  [r.randint(10, (w//2)-250), r.randint(10, (h//2)+250)], [r.randint((w//2)+250, w-10), r.randint((h//2)+250, h-10)]])
        self.acceleration = acceleration

        self.rect        = self.image.get_rect(center = self.position)

        self.angle       = r.randint(0, 359)                     # current heading (deg)
        self.angular_vel = angular_vel                 # deg / 
        self.orientation = [m.sin(m.radians(self.angle)), m.cos(m.radians(self.angle))]

        self.limits = (w, h)
        
        
    def getposition(self):
        return self.position
    def getrect(self):
        return self.rect
    # ------------------------------------------------------------------
    def _build_asteroid_surface(self) -> pygame.Surface:
        points = [(0, 200),(50, 100),(100, 80),(150,25),(200,50),(250,0),(350, 40),(480,150),
                  (450,250),(475,350),(400, 450),(250,500),(50,400),(5,300)]
        details1 = [(50, 100),(200,150),(250, 200)]
        details2 = [(475,350),(400,400),(375,350),(300,300),(290, 300),(270, 270)]
        surf   = pygame.Surface((500, 500), pygame.SRCALPHA)
        
        #for i in range(0, 500, 50):
        #    pygame.draw.line(surf, (200, 200, 200), (0, i), (500, i), 2)      <- this commented block s for debugging collisions
        #    pygame.draw.line(surf, (200, 200, 200), (i, 0), (i, 500), 2)
        #pygame.draw.circle(surf, (100, 100, 255, 50), (250, 250), 250, 5)

        pygame.draw.lines(surf, (0, 255, 100), True, points, 5)
        pygame.draw.lines(surf, (0, 255, 100), False, details1, 5)
        pygame.draw.lines(surf, (0, 255, 100), False, details2, 5)
        return surf

    # ------------------------------------------------------------------
    def update(self, dt: float, position: int):
        """Advance the rotation based on elapsed time (`dt` in seconds)."""
        self.angle = (self.angle + self.angular_vel * dt) % 360 
        self.image = pygame.transform.rotate(self._orig_image, self.angle)

        self.rect.x += self.orientation[0] * self.acceleration
        self.rect.y += self.orientation[1] * self.acceleration

        # re‑centre after the size change caused by rotation
        self.rect = self.image.get_rect(center = self.rect.center)
        paralax.InfiniteParalax.is_offlimits(self)
    # ------------------------------------------------------------------
    def draw(self, target: pygame.Surface) -> None:
        """Blit the current image onto *target*."""
        target.blit(self.image, self.rect)
