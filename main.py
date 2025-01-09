from utils import load_images

import pygame as pg

from typing import Final


pg.init()

SCREEN_SIZE: Final[tuple[int]] = (800, 600)
FPS: Final[int] = 30

screen: pg.display = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Flickering candle")

clock: pg.time.Clock = pg.time.Clock()
stop: bool = False

images: list[pg.Surface] = load_images(path="")

def event_handler() -> None | bool:
    """ Handles all the events. """
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return True
        
def draw_window(screen) -> None:
    """ Draws the window. """
    screen.fill((0, 0, 0))
    for i in range(100):
        pg.draw.line(screen, (255 - i * 2, 255 - i * 2, 255 - i * 2), (350 + i, 400), (350 + i, 600))

    pg.display.update()

if __name__ == "__main__":
    while not stop:
        clock.tick(FPS)
        stop = event_handler()
        draw_window(screen)




