import random
import asyncio
import time

from Obstacle import Obstacle
from setting import *
from Player import Player

pg.init()

screen = pg.display.set_mode((setting['w'], setting['h']))
pg.display.set_caption(setting['title'])

clock = pg.time.Clock()

obstacle_group = pg.sprite.Group()
all_sprite = pg.sprite.Group()

player = Player()
all_sprite.add(player)

font = pg.font.Font(decrypted, 100)
text_surface = font.render("Game Over", True, (255, 255, 255))
text_center = text_surface.get_rect().center
center_t_x, center_t_y = text_center

score_font = pg.font.Font(decrypted, 70)
score_surface = font.render('0', True, (255, 255, 255))


def new_mobs():
    obstacle_bottom = Obstacle(setting['w'], random.randint(-100, 100))
    obstacle_top = Obstacle(setting['w'], random.randint(500, setting['h']))
    obstacle_group.add(obstacle_top, obstacle_bottom)
    all_sprite.add(obstacle_group)


SPAWN_SPRITE = pg.USEREVENT + 1
pg.time.set_timer(SPAWN_SPRITE, 1500)

pg.time.set_timer(pg.USEREVENT, 50)

run = True

score = 0
while run:

    clock.tick(setting['fps'])
    pg.display.flip()
    screen.blit(background_img, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == SPAWN_SPRITE:
            new_mobs()
        if event.type == pg.USEREVENT:
            score_surface = font.render(f"{score}", True, 'white')
            score += 1

    all_sprite.update()
    all_sprite.draw(screen)

    if pg.sprite.spritecollide(player, obstacle_group, False, pg.sprite.collide_circle):
        screen.blit(text_surface, (300 - center_t_x, 300 - center_t_y))
        run = False

    screen.blit(score_surface, (300, 20))

    pg.display.flip()

pg.quit()
