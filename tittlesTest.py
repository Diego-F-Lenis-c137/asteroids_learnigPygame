import pygame as p
import time as t
import tittles as tts
from screeninfo import get_monitors

p.init()

def get_display_size():
    mon = next((m for m in get_monitors() if m.is_primary), None)
    return (mon.width, mon.height) if mon else (1280, 720)

w, h = get_display_size()


screen = p.display.set_mode((w, h), p.FULLSCREEN)
p.display.set_caption("Test Title")

titles = (tts.Start(w, h), tts.died(w, h), tts.gameOver(w, h))

running = True
while running:
    
    for e in p.event.get():
        if (e.type == p.QUIT or 
            (e.type == p.KEYDOWN and e.key == p.K_ESCAPE)):
            
            running = False
    
    for img in titles:
        screen.fill((0,0,0))
        screen.blit(img, img.get_rect(center=img.get_rect().center))
        p.display.flip()
        t.sleep(2)
        