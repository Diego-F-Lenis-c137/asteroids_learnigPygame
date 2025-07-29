# shoot.py
import pygame
import math as m
import infiniteparalax as paralax

class Shoot(pygame.sprite.Sprite):

    def __init__(self, obj):
        super().__init__()
        self.obj = obj
        self._orig_image = self._build_shoot_surface()  # cache the artwork
        self.speed = 5  # Reduced speed for better control
        self.angle = obj.angle
        self.orientation = obj.orientation.copy()  # Make a copy to avoid reference issues
        self.limits = (obj.w, obj.h)
        self.image = pygame.transform.rotate(self._orig_image, self.angle)
        self.rect = self.image.get_rect(center=obj.rect.center)  # Use rect.center for proper positioning
        
        # Use pygame.math.Vector2 for precise position tracking
        self.position = pygame.math.Vector2(self.rect.center)
        
        # Maximum distance before bullet is destroyed
        self.max_distance = 800
        self.distance_traveled = 0
        
        ###print(f'Bullet initialized at {self.position}')

    def getposition(self):
        return self.position
    
    def getrect(self):
        return self.rect
    
    # ------------------------------------------------------------------
    def _build_shoot_surface(self) -> pygame.Surface:
        """Draw a small bullet surface."""
        surf = pygame.Surface((4, 8), pygame.SRCALPHA)
        pygame.draw.rect(surf, (255, 255, 0), (0, 0, 4, 8))  # Yellow bullet
        return surf

    # ------------------------------------------------------------------
    def update(self):
        """Update bullet position each frame."""
        # Move the bullet
        movement = pygame.math.Vector2(self.orientation[0] * self.speed, 
                                      self.orientation[1] * self.speed)
        self.position += movement
        self.distance_traveled += movement.length()
        
        # Update rect position
        self.rect.x += self.orientation[0] * self.speed
        self.rect.y += self.orientation[1] * self.speed

        ###self.rect.center = (int(self.position.x), int(self.position.y)) <- old, bugged infinite paralax
        paralax.InfiniteParalax.is_offlimits(self)
        # Check if bullet should be destroyed
        if (self.distance_traveled > self.max_distance):
            self.kill()
       # 
    # ------------------------------------------------------------------
    def draw(self, target: pygame.Surface) -> None:
        """Blit the current image onto *target*."""
        target.blit(self.image, self.rect)


#/// GPT's sugestion, read carefully
'''
class Shoot(pygame.sprite.Sprite):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj
        self._orig_image = self._build_shoot_surface()
        self.speed = 10
        self.angle = obj.angle
        self.orientation = obj.orientation
        self.limits = (obj.w, obj.h)

        self.image = pygame.transform.rotate(self._orig_image, -self.angle)
        self.rect = self.image.get_rect(center=obj.position)
        self.position = pygame.math.Vector2(self.rect.center)

    def _build_shoot_surface(self) -> pygame.Surface:
        surf = pygame.Surface((4, 4), pygame.SRCALPHA)
        pygame.draw.circle(surf, (255, 0, 0), (2, 2), 2)
        return surf

    def update(self):
        # Move in the direction of orientation
        dx = self.orientation[0] * self.speed
        dy = self.orientation[1] * self.speed
        self.position.x += dx
        self.position.y += dy
        self.rect.center = (int(self.position.x), int(self.position.y))

        # Wrap around the screen if needed
        self.position.x %= self.limits[0]
        self.position.y %= self.limits[1]

        # Optional: remove the bullet if it's gone too far
        # or implement some time-to-live logic here

    def draw(self, target: pygame.Surface):
        target.blit(self.image, self.rect)
'''