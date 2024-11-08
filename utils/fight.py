import pygame

def draw_fight(win, width, height):
    fight_img = pygame.image.load('assets/fight.jpg')
    fight_img = pygame.transform.scale(fight_img, (500, 300))
    win.blit(fight_img, (width / 2 - fight_img.get_width() / 2, height / 2 - fight_img.get_height() / 2))
    fight_surface = pygame.Surface((400, 200), pygame.SRCALPHA)
    fight_surface.set_alpha(100)
    fight_surface.fill((0, 0, 0))
    win.blit(fight_surface, (width / 2 - fight_img.get_width() / 2, height / 2 - fight_img.get_height() / 2))