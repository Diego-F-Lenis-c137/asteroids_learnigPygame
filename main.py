
import pygame
import time
from screeninfo import get_monitors

from ship import Ship
from asteroid import Asteroid
from controls import Controls
from backgrounderizer import Backgrounderizer as bgnd
import tittles
# ----------------------------------------------------------------------
COLLISION_RATIO = 0.70721357850070721357850070721358  # Adjust this value as needed for collision sensitivity
def get_display_size():
    mon = next((m for m in get_monitors() if m.is_primary), None)
    return (mon.width, mon.height) if mon else (1280, 720)
def subdivision(asteroid, size, pos):
    asteroids.add(list(asteroid.subdivide(size-1, pos)))
    asteroids.remove(asteroid)

def gameOver(screen):
    screen.blit(tittles.gameOver(screen.get_width(), screen.get_height()), (0, 0))
    pygame.display.flip()
    time.sleep(3)
    running = False

# ----------------------------------------------------------------------
def main():
    pygame.init()
    
    lives = 3
    level = 1
    n = 5
    W, H   = get_display_size()
    screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
    pygame.display.set_caption("Rocas del espacio - alpha 2.0")

    clock  = pygame.time.Clock()

    pos = (W // 2, H // 2)
    
    
    ship = Ship(W, H, screen, angular_vel=360.0)

    ships = pygame.sprite.Group()
    ships.add(ship)

    global asteroids 
    asteroids = pygame.sprite.Group()
    [asteroids.add(Asteroid(3, W, H, None)) for _ in range(n)]
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
        shp = pygame.sprite.groupcollide(ships, asteroids,  True,  False, collided=pygame.sprite.collide_circle_ratio(COLLISION_RATIO)) 
        for ship, asteroid in shp.items():
                ship.shoots = False
                del ship

                lives -= 1
                if lives >= 0:
                    ship = Ship(W, H, screen, angular_vel=360.0)
                    ships.add(ship)
                    ship.rect = ship.image.get_rect(center = pos) 
                    controller = Controls(ship)
                else:
                    
                    time.sleep(1)
                    gameOver(screen)
                
       
        ast = pygame.sprite.groupcollide(asteroids, bullets, False,  True, collided=pygame.sprite.collide_circle_ratio(COLLISION_RATIO))
        for asteroid, bullet in ast.items():
            
            if asteroid.size > 1:
                asteroids.add(list(asteroid.subdivide(asteroid.size-1, asteroid.position)))
                asteroids.remove(asteroid)
                del asteroid
                #Asteroid.subdivide(asteroid, asteroid.size, asteroid.position)
            else:
                asteroid.kill() 

        #print(len(asteroids))
        if (len(asteroids) <= 0):
            level += 0.2
            ship.rect.x, ship.rect.y = [W//2, H//2]
            [asteroids.add(Asteroid(3, W, H, None)) for _ in range(n)]
            
        dt = clock.tick(60) / 1000.0        # seconds since last frame
        ships.update(dt, 0)  # Pass 0 instead of undefined variable
        asteroids.update(dt)  
        # Update all bullets
        bullets.update()
        
        screen.fill((0, 0, 0))
        background.draw(dt)
        ships.draw(screen)
        
        # Draw all bullets
        bullets.draw(screen)
        
        [asteroid.draw(screen) for asteroid in asteroids if asteroid.size >= 1   ]
        pygame.display.flip()

    pygame.quit()
  
if __name__ == "__main__":
    
    main()
