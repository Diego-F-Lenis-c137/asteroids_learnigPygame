# ship.py
import pygame
import math as m
import random as r
import infiniteparalax as paralax

class Asteroid(pygame.sprite.Sprite):

    def __init__(self, w, h, angular_vel=30.0):
        super().__init__()
        self._orig_image = self._build_asteroid_surface()  # cache the artwork
        self.image       = pygame.transform.rotate(self._orig_image, angular_vel)            # what gets blitted
        self.position = [r.randint(10, w-10), r.randint(10, h-10)]

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
        """Draw the red polyline on a transparent surface once."""
        points = [(0 , 200),(50,100),(100,50),(160,50),(250,55),(450,160),
                  (400,250),(500,400),(250,500),(50,400),(4,300 )]
        details1 = [(250,55),( 200 ,160),(150, 200 )]
        details2 = [(500,400),(300,300),(290,200),(150,350)]
        surf   = pygame.Surface((500, 500), pygame.SRCALPHA)
        #pygame.draw.circle(surf, (0, 255, 100), (200, 200), 200, 3)
        pygame.draw.lines(surf, (0, 255, 100), True, points, 5)
        pygame.draw.lines(surf, (0, 255, 100), False, details1, 5)
        pygame.draw.lines(surf, (0, 255, 100), False, details2, 5)
        return surf

    # ------------------------------------------------------------------
    def update(self, dt: float, position: int):
        """Advance the rotation based on elapsed time (`dt` in seconds)."""
        self.angle = (self.angle + self.angular_vel * dt) % 360 
        self.image = pygame.transform.rotate(self._orig_image, self.angle)

        self.rect.x += self.orientation[0] 
        self.rect.y += self.orientation[1] 

        # re‑centre after the size change caused by rotation
        self.rect = self.image.get_rect(center = self.rect.center)
        paralax.InfiniteParalax.is_offlimits(self)
    # ------------------------------------------------------------------
    def draw(self, target: pygame.Surface) -> None:
        """Blit the current image onto *target*."""
        target.blit(self.image, self.rect)
