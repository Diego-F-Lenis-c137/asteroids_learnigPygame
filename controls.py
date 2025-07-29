
import normalizer
import math as m
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT,KEYDOWN, KEYUP, K_SPACE

class Controls():
    def __init__(self, ship):
        self.F = K_UP
        self.B = K_DOWN
        self.R = K_RIGHT
        self.L = K_LEFT
        self.S = K_SPACE
        self.ship = ship

    def update(self, e):
        
        if (e.type == KEYDOWN):
            match e.key:
                case self.F:
                    self.ship.forward = True
                case self.B:
                    self.ship.backward = True
                case self.R:
                    self.ship.right = True
                case self.L:
                    self.ship.left = True
                case K_SPACE:
                    
                    return self.ship.shoot()  # Return the bullet object

        elif e.type == KEYUP:
            match e.key:
                case self.F:
                    self.ship.forward = False
                case self.B:
                    self.ship.backward = False
                case self.R:
                    self.ship.right = False
                case self.L:
                    self.ship.left = False
        
        return None  # Return None when no bullet is created

