# main.py
import pygame
from screeninfo import get_monitors

from ship import Ship
from asteroid import Asteroid
from controls import Controls
from backgrounderizer import Backgrounderizer as bgnd
# ----------------------------------------------------------------------
COLLISION_RATIO = 0.70721357850070721357850070721358  # Adjust this value as needed for collision sensitivity
def get_display_size():
    mon = next((m for m in get_monitors() if m.is_primary), None)
    return (mon.width, mon.height) if mon else (1280, 720)

# ----------------------------------------------------------------------
def main():
    level = 1
    pygame.init()
    W, H   = get_display_size()
    screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
    pygame.display.set_caption("Rocas del espacio - alpha 2.0")

    clock  = pygame.time.Clock()

    pos = (W // 2, H // 2)
    ship = Ship(W, H, screen, angular_vel=360.0)
    ships = pygame.sprite.Group()
    ships.add(ship)
    asteroids = pygame.sprite.Group()
    asteroids.add(Asteroid(W, H), Asteroid(W, H), Asteroid(W, H), Asteroid(W, H))
    background = bgnd((W,H), screen)
    ship.rect = ship.image.get_rect(center = pos) 
    controller = Controls(ship)
    
    # Create sprite groups for bullet management
    bullets = pygame.sprite.Group()

    running = True
    while running:
       
        for e in pygame.event.get():
            if (e.type == pygame.QUIT or 
               (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE)):
                
                running = False
            
            # Handle shooting - get the bullet from controller and add to group
            bullet = controller.update(e)
            if bullet:
                bullets.add(bullet)
                 
        pygame.sprite.groupcollide(asteroids, ships,  False,  True, collided=pygame.sprite.collide_circle_ratio(COLLISION_RATIO)) 
        pygame.sprite.groupcollide(bullets, asteroids, True,  True, collided=pygame.sprite.collide_circle_ratio(COLLISION_RATIO))

        if (len(asteroids) <= 0):
            level += 0.2
            ship.rect.x, ship.rect.y = [W//2, H//2]
            asteroids.add(Asteroid(W, H, acceleration=level), Asteroid(W, H, acceleration=level), Asteroid(W, H, acceleration=level), Asteroid(W, H, acceleration=level))

        dt = clock.tick(60) / 1000.0        # seconds since last frame
        ship.update(dt, 0)  # Pass 0 instead of undefined variable
        asteroids.update(dt, 0)  
        
        # Update all bullets
        bullets.update()
        
        screen.fill((0, 0, 0))
        background.draw(dt)
        ship.draw(screen)
        
        # Draw all bullets
        bullets.draw(screen)
        asteroids.draw(screen)
        
        pygame.display.flip()

    pygame.quit()
  
if __name__ == "__main__":
    
    main()
