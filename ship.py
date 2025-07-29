# ship.py
import pygame
import math as m
import infiniteparalax as paralax
import shoot as s

class Ship(pygame.sprite.Sprite):

    def __init__(self, w, h, screen, angular_vel=30.0):
        super().__init__()
        self.screen =screen
        self._orig_image = self._build_ship_surface()  # cache the artwork
        self.image       = pygame.transform.rotate(self._orig_image, 45.0)            # what gets blitted
        self.position = [0,0]
        self.rect        = self.image.get_rect(center = self.position)

        self.angle       = 0.0                         # current heading (deg)
        self.angular_vel = angular_vel                 # deg / 
        self.speed = 10
        
        self.orientation = [m.cos(self.angle), m.sin(self.angle)]
        self.right = False
        self.left = False
        self.forward = False
        self.backward= False
        self.w = w
        self. h = h
        self.limits = (w, h)
        
    def shoot(self):
        # Create a new bullet and return it to be added to the bullet group
        return s.Shoot(self)

    def getposition(self):
        return self.position
    def getrect(self):
        return self.rect
    # ------------------------------------------------------------------
    def _build_ship_surface(self) -> pygame.Surface:
        """Draw the red polyline on a transparent surface once."""

        points = [(0, 0), (25, 25), (50, 0), (25, 75)]
        surf   = pygame.Surface((50, 75), pygame.SRCALPHA)
        pygame.draw.lines(surf, (255, 0, 0), True, points, 5)
        return surf

    # ------------------------------------------------------------------
    def update(self, dt: float, position: int):
        """Advance the rotation based on elapsed time (`dt` in seconds)."""
        self.angle = (((self.angle - self.angular_vel * dt) % 360) if self.right else (((self.angle + self.angular_vel * dt) % 360) if self.left else self.angle))
        self.image = pygame.transform.rotate(self._orig_image, self.angle)
        if self.forward:
            self.rect.x += self.orientation[0] * self.speed
            self.rect.y += self.orientation[1] * self.speed
        elif self.backward:
            self.rect.x -= self.orientation[0] * self.speed
            self.rect.y -= self.orientation[1] * self.speed

        # re‑centre after the size change caused by rotation
        self.rect = self.image.get_rect(center = self.rect.center)
        
        self.orientation = [m.sin(m.radians(self.angle)), m.cos(m.radians(self.angle))]
        paralax.InfiniteParalax.is_offlimits(self)
       
    # ------------------------------------------------------------------
    def draw(self, target: pygame.Surface) -> None:
        """Blit the current image onto *target*."""
        target.blit(self.image, self.rect)
