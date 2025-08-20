import pygame as p
from pygame import font as pfont
pfont.init()

font = p.font.Font("PK.TTF", 72)

titletext = font.render("Rock Paper Ships", True, (255, 255, 0))
titletext2 = font.render("Start", True, (255, 255, 0))

deathtext = font.render("U DIED", True, (255, 100, 100))

game = font.render("game", True, (255, 0, 0))
over = font.render("over", True, (255, 0, 0))


def Start(w, h):
    srf = p.Surface((w,h), p.SRCALPHA)
    rect = srf.get_rect(center=(w//2, h//2))
    rect.width //= 2
    rect.height //= 2
    rect.x = w//2 - rect.width//2
    rect.y = h//2 - rect.height//2
    color = ((0,255,0))
    p.draw.rect(srf, color, rect, width = 3, border_radius = 20)


    srf.blit(titletext, titletext.get_rect(center=(w//2,h//2 - 50)))
    srf.blit(titletext2, titletext2.get_rect(center=(w//2,h//2 + 60)))
    return srf

def died(w, h):
    srf = p.Surface((w,h), p.SRCALPHA)
    rect = srf.get_rect(center=(w//2, h//2))
    rect.width = w//5
    rect.height = h//5
    rect.x = w - w//5 - rect.width//2
    rect.y = h//5 - rect.height//2

    color = ((255,0,255))
    p.draw.rect(srf, color, rect, width = 3, border_radius = 20)
    srf.blit(deathtext, deathtext.get_rect(center=rect.center))
    return srf

def gameOver(w, h):
    srf = p.Surface((w,h), p.SRCALPHA)
    rect = srf.get_rect(center=(w//2, h//2))
    rect.width //= 2
    rect.height //= 2
    rect.x = w//2 - rect.width//2
    rect.y = h//2 - rect.height//2
    color = ((255,0,0))

    p.draw.rect(srf, color, rect, width = 3, border_radius = 20)

    srf.blit(game, game.get_rect(center=(w//2,h//2 - 50)))
    srf.blit(over, over.get_rect(center=(w//2,h//2 + 60)))
    return srf