# ship.py
import pygame
import math as m
import random as r
import infiniteparalax as paralax

class Asteroid(pygame.sprite.Sprite):

    def __init__(self, size, w, h, position, acceleration = 1.0, angular_vel=30.0):
        super().__init__()
        self.size = size
        if size <1:
            self.kill()
            del self

        if size >= 1:    
            if size == 3:
                self.position = r.choice([[r.randint(10, (w//2)-250), r.randint(10, (h//2)-250)], [r.randint((w//2)+250, w-10), r.randint((h//2)-250, h-10)],
                                        [r.randint(10, (w//2)-250), r.randint(10, (h//2)+250)], [r.randint((w//2)+250, w-10), r.randint((h//2)+250, h-10)]])
            else:
                self.position = [position[0]+ 250, position[1]+250] if size == 2 else [position[0]+ 50, position[1]+50]
            #self.position = [w//2, h//2]

            self._orig_image = self._build_asteroid_surface(size)  # cache the artwork
            self.image       = self._orig_image          # what gets blitted

            self.acceleration = (acceleration*3)//size


            self.rect        = self.image.get_rect(center = self.position)

            self.angle       = r.choice([r.randint(1, 89), r.randint(91, 179), r.randint(181, 269), r.randint(271, 359)])
            self.angular_vel = angular_vel                 # deg / 
            self.orientation = [m.sin(m.radians(self.angle)) * self.acceleration, m.cos(m.radians(self.angle)) * self.acceleration]

            self.limits = (w, h)
            self.w = w
            self.h = h

    def subdivide(self, size, pos):
        return Asteroid(size, self.w, self.h, pos, acceleration=self.acceleration, angular_vel=self.angular_vel), Asteroid(size, self.w, self.h, pos, acceleration=self.acceleration, angular_vel=self.angular_vel)

    def getposition(self):
        return self.position
    def getrect(self):
        return self.rect
    # ------------------------------------------------------------------
    def _build_asteroid_surface(self, size) -> pygame.Surface:

        if size == 3:
            
            surf   = pygame.Surface((500, 500), pygame.SRCALPHA)
            #surf.fill((255,255,255))
            points = [(0, 200),(50, 100),(100, 80),(150,25),(200,50),(250,0),(350, 40),(480,150),
                    (450,250),(475,350),(400, 450),(250,500),(50,400),(5,300)]
            details1 = [(50, 100),(200,150),(250, 200)]
            details2 = [(475,350),(400,400),(375,350),(300,300),(290, 300),(270, 270)]
            
            #for i in range(0, 500, 50):
            #    pygame.draw.line(surf, (200, 200, 200), (0, i), (500, i), 2)      #<- this commented block s for debugging collisions
            #    pygame.draw.line(surf, (200, 200, 200), (i, 0), (i, 500), 2)

            #pygame.draw.circle(surf, (100, 100, 255, 50), (250, 250), 250, 5)
            pygame.draw.lines(surf, (0, 255, 100), True, points, 5)
            pygame.draw.lines(surf, (0, 255, 100), False, details1, 5)
            pygame.draw.lines(surf, (0, 255, 100), False, details2, 5)
            return surf
        elif size == 2:
            
            surf   = pygame.Surface((250, 250), pygame.SRCALPHA)
            points = [(0, 100),(100, 80),(150,25),(200,50),(240,150),
                    (225,190),(50,200),(5,150)]
            details1 = [(150,25),(100,5),(50,25),(25,90),(50, 100),
                        (200,150),(225, 200),(125, 240),(50, 200)]
            
            #for i in range(0, 250, 25):
            #    pygame.draw.line(surf, (200, 200, 200), (0, i), (250, i), 2)      #<- this commented block s for debugging collisions
            #    pygame.draw.line(surf, (200, 200, 200), (i, 0), (i, 250), 2)

            #pygame.draw.circle(surf, (100, 100, 255, 50), (125, 125), 125, 5)
            pygame.draw.lines(surf, (0, 255, 100), True, points, 5)
            pygame.draw.lines(surf, (0, 255, 100), False, details1, 5)
            return surf
        elif size == 1:
            
            surf   = pygame.Surface((100, 100), pygame.SRCALPHA)
            points = [(0, 40),(40, 30),(60,10),(80,20),(85,40),
                    (90,60),(20,80),(5,60)]
            details1 = [(50, 40),(80,50),(90, 70),(60,90),(30, 75)]
            details2 = [(10, 40),(20,20),(40,10),(50,20)]
            
            #for i in range(0, 100, 10):
            #    pygame.draw.line(surf, (200, 200, 200), (0, i), (100, i), 2)
            #    pygame.draw.line(surf, (200, 200, 200), (i, 0), (i, 100), 2)
            
            #pygame.draw.circle(surf, (100, 100, 255, 50), (50, 50), 50, 5)
            pygame.draw.lines(surf, (0, 255, 100), True, points, 3)
            pygame.draw.lines(surf, (0, 255, 100), False, details1, 3)
            pygame.draw.lines(surf, (0, 255, 100), False, details2, 3)
            return surf            
        else:
            # Handle unexpected sizes
            print(f"Unexpected asteroid size: {size}")
           

    # ------------------------------------------------------------------
    def update(self, dt: float):
        """Advance the rotation based on elapsed time (`dt` in seconds)."""
        
        self.angle = (self.angle + self.angular_vel * dt) % 360 
        self.image = pygame.transform.rotate(self._orig_image, self.angle)

        self.rect.x += self.orientation[0]
        self.rect.y += self.orientation[1]
        self.position = [self.rect.x, self.rect.y]

        self.rect = self.image.get_rect(center = self.rect.center)

        paralax.InfiniteParalax.is_offlimits(self)
    

    # ------------------------------------------------------------------
    def draw(self, target: pygame.Surface) -> None:
        """Blit the current image onto *target*."""
        target.blit(self.image, self.rect)
