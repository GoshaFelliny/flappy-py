import pygame as pg

bird_images = [pg.image.load(f'birds/bird{i}.png') for i in range(1, 4)]
pg.mixer.init()
sound = pg.mixer.Sound('sfx_wing.mp3')


class Bird(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('birds/bird1.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.vector = 2
        self.jump_time = None

    def jump(self):
        self.vector = -5
        self.jump_time = pg.time.get_ticks()
        self.image = pg.image.load('birds/bird4.png')
        sound.play()

    def update(self):

        self.rect.y += self.vector
        if self.rect.bottom > 600:
            self.rect.bottom = 600

        if self.rect.top < 0:
            self.rect.top = 0

        if self.jump_time is not None:
            elapsed_time = pg.time.get_ticks() - self.jump_time
            if elapsed_time >= 300:
                self.vector = 2
                current_time = pg.time.get_ticks()
                frame_duration = 200  # Задержка между кадрами в миллисекундах
                frame_index = (current_time // frame_duration) % len(bird_images)
                self.image = bird_images[frame_index]
