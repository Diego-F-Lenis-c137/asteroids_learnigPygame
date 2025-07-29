import pygame, time

from screeninfo import get_monitors

primary_monitor = next((m for m in get_monitors() if m.is_primary), None)

W = primary_monitor.width
H = primary_monitor.height
primary_monitor.x, primary_monitor.y
primary_monitor.width / primary_monitor.height

def ship():
    points = [(0, 0), (25, 25), (50, 0), (25, 75)]
    s = pygame.Surface((50, 75), pygame.SRCALPHA)     # allow alpha
    pygame.draw.lines(s, (255, 0, 0), True, points, 5)
    return s



pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Expreimenting with window attributes")
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
custom_surface = pygame.Surface((200, 100))

clock         = pygame.time.Clock()
ship_image    = ship()
ship_rect     = ship_image.get_rect(center=(W // 2, H // 2))
angle         = 0.0
ANGULAR_VEL   = 30.0 
#pygame.draw.line(screen, GREEN, [width/2, height/2], [100, 100], 5)
#pygame.draw.lines(screen, RED, True, ship(([width/2, height/2]), ), 5)



# Main loop flag
running = True

# Main loop
while running:
    # Event handling
    for event in pygame.event.get():
        # Check for window close event
        if event.type == pygame.QUIT:
            # Exit the loop
            running = False

    # Update the display

    dt = clock.tick(60) / 1000.0 
    angle = (angle + ANGULAR_VEL * dt) % 360
    screen.fill((0, 0, 0))
    rotated   = pygame.transform.rotate(ship_image, angle)
    rot_rect  = rotated.get_rect(center=ship_rect.center)
    screen.blit(rotated, rot_rect)

    pygame.display.flip()

pygame.quit()