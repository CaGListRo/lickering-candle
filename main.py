from utils import load_images
from utils import Slider

import pygame as pg

from random import uniform, randint
from time import perf_counter
from typing import Final


pg.init()

SCREEN_SIZE: Final[tuple[int]] = (800, 600)
screen: pg.display = pg.display.set_mode(SCREEN_SIZE)

stop: bool = False

images: list[pg.Surface] = load_images(path="")

min_slider: Slider = Slider(slider_type="MIN", min_pos=10, max_pos=110, value=0.01, min_value=0.0, max_value=0.2, y_pos=500)
max_slider: Slider = Slider(slider_type="MAX", min_pos=10, max_pos=110, value=0.2, min_value=0.2, max_value=1.0, y_pos=530)

def event_handler() -> None | bool:
    """ Handles all the events. """
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return True
        
def draw_window(screen: pg.display, image: pg.Surface, image_transparency: int, fps: int) -> None:
    """ Draws the window. """
    # set caption with fps
    pg.display.set_caption(f"Flickering candle          FPS: {fps}")

    # fill the screen with gray
    screen.fill((100, 100, 100))

    # draw wig
    pg.draw.rect(screen, (0, 0, 0), (395, 380, 10, 23), 5, 1)

    # draw candle
    for i in range(100):
        pg.draw.line(screen, (255 - i * 2, 255 - i * 2, 255 - i * 2), (350 + i, 400), (350 + i, 600))
    
    # draw flame
    flame_x: int = 395 - 34  # calculate the x position
    flame_y: int = int(395 - image.get_height())
    image.set_alpha(image_transparency)
    screen.blit(image, (flame_x, flame_y))

    # draw sliders
    min_slider.render(screen)
    max_slider.render(screen)

    pg.display.update()

if __name__ == "__main__":
    # old time for delta time calculation
    old_time: float = perf_counter()
    # fps stuff
    fps_timer: float = 0.0
    fps_counter: int = 0
    fps: int = 0
    # choose an image
    image_number: int = randint(0, 11)
    # old image to avoid doubles
    old_image_number: int = image_number
    # set the image transparency
    image_transparency: int = randint(150, 255)
    # to make the candle flicker
    min_value: float = 0.01
    max_value: float = 0.2
    flicker_timer: float = 0.0
    flicker_time: float = uniform(min_value, max_value)
    while not stop:
        # calculate delta time
        dt: float = perf_counter() - old_time
        old_time = perf_counter()
        # count the frames
        fps_counter += 1
        # increase the fps timer
        fps_timer += dt
        if fps_timer >= 1:
            fps = fps_counter  
            fps_counter = 0
            fps_timer = 0
        stop = event_handler()
        draw_window(screen, images[image_number], image_transparency, fps)
        flicker_timer += dt
        if flicker_timer >= flicker_time:
            flicker_timer = 0.0
            #while image_number == old_image_number:
            image_number: int = randint(0, 11)           
            old_image_number: int = image_number
            if min_slider.check_collision():
                min_value = min_slider.get_value()
            if max_slider.check_collision():
                max_value = max_slider.get_value()
            flicker_time: float = uniform(min_value, max_value)
            image_transparency: int = randint(150, 255)







