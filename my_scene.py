from setting import *


def lose_game(score: int):
    pg.font.init()
    font = pg.font.Font(decrypted, 100)
    text_surface = font.render("Game Over", True, (255, 255, 255))

    score_font = pg.font.Font(decrypted, 70)

    wait = True
    screen = pg.display.set_mode((setting['w'], setting['h']))
    pg.display.set_caption(setting['title'])

    while wait:
        clock.tick(setting['fps'])
        screen.blit(background_img, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                wait = False

        score_surface = score_font.render(f"{score}", True, (255, 255, 255))

        screen.blit(text_surface, (180, 100))
        screen.blit(score_surface, (300, 180))

        pg.display.flip()

    pg.quit()
