from setting import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.speedx = None
        self.images = [player_img, player_img2]  # кадры
        self.animation_time = 3000  # время смены кадров
        self.index = 0  # текущий кадр
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = 400, 400
        self.last_update = pg.time.get_ticks()

    def update(self):

        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -8
        if keystate[pg.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx

        if keystate[pg.K_SPACE]:
            self.rect.y -= 40

        if self.rect.x > setting['w'] - 42:
            self.rect.x -= 10
        if self.rect.x < 0:
            self.rect.x += 10

        if self.rect.bottom < setting['h']:
            self.rect.y += 5

        else:
            self.rect.bottom = setting['h']

        if self.rect.top < 0:
            self.rect.top = 0


