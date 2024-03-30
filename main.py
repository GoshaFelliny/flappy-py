import random

import pygame as pg
from bird import Bird
from pipe import Pipe

pg.init()
pg.font.init()

font = pg.font.SysFont("None", 100)

W, H = 600, 600

screen = pg.display.set_mode((W, H))

bird = Bird(50, H // 2)

all_sprite = pg.sprite.Group(bird)
pipes = pg.sprite.Group()

run = True

clock = pg.time.Clock()

pg.time.set_timer(pg.USEREVENT, 2000)
pg.time.set_timer(pg.USEREVENT+1, 2000)

score = 0
pipe_scored = False

back_ground_img = pg.image.load('flappy bird.png')
back_ground = pg.surface.Surface((back_ground_img.get_width(), 600))
back_ground_x = 0
back_ground_x2 = back_ground_img.get_width()

while run:

    screen.fill('white')
    clock.tick(60)


    back_ground.blit(back_ground_img, (0, 0))
    screen.blit(back_ground, (back_ground_x, 0))
    screen.blit(back_ground, (back_ground_x2, 0))

    back_ground_x -= 1
    back_ground_x2 -= 1

    if back_ground_x < -back_ground_img.get_width():
        back_ground_x = back_ground_img.get_width()

    if back_ground_x2 < -back_ground_img.get_width():
        background_x2 = back_ground_img.get_width()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYUP and event.key == pg.K_SPACE:
            bird.jump()
        if event.type == pg.USEREVENT:
            rand_hight = 150 + random.randint(0, 50)
            pipe_up = Pipe(W, 0, 50, rand_hight, (129, 208, 58))
            pipe_down = Pipe(W, rand_hight + random.randint(100, 200), 50, 1000, (129, 208, 58))
            all_sprite.add(pipe_up, pipe_down)
            pipes.add(pipe_up, pipe_down)
        if event.type == pg.USEREVENT + 1:
            score += 1

    if pg.sprite.spritecollide(bird, pipes, False):
        run = False

    all_sprite.draw(screen)
    all_sprite.update()

    text = font.render(f"{score}", False, 'white')
    screen.blit(text, (W // 2 - 25, 500))

    pg.display.update()

pg.quit()
