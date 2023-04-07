import os
import pygame as pg

setting = {
    'w': 600,
    'h': 600,
    'title': 'Test',
    'fps': 30,
}

game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder, 'media')
font_folder = os.path.join(game_folder, 'font')

player_img = pg.image.load(os.path.join(media_folder, 'player.png'))
player_img2 = pg.image.load(os.path.join(media_folder, 'player2.png'))

obstacle_img = pg.image.load(os.path.join(media_folder, 'obstacle.png'))
background_img = pg.image.load(os.path.join(media_folder, 'Iast1tOF9yA.jpg'))

decrypted = os.path.join(font_folder, 'Decrypted.ttf')
clock = pg.time.Clock()
