import pygame as pg
import os
from typing import Final


IMAGE_BASE_PATH: Final[str] = "images/"
def load_image(img_name: str) -> pg.surface:
    """
    Loads an image from the given path and scales it by the given factor. 
    Args:
    img_name (str): The name of the image to load.
    scale_factor (float): The factor to scale the image by.
    """
    try:
        img = pg.image.load(IMAGE_BASE_PATH + img_name).convert_alpha()
    except FileNotFoundError as e:
        print(f"Error: {e}")
    return img

def load_images(path: str) -> pg.surface:
    """
    Loads all images from the given path and scales them by the given factor with the 'load_image' function.
    Args:
    path (str): The path to the images.
    scale_factor (float): The factor to scale the images by.
    """
    images = []
    for img_name in sorted(os.listdir(IMAGE_BASE_PATH + path)):
        images.append(load_image(img_name=path + "/" + img_name))
    return images


class Slider:
    def __init__(self, slider_type: str, min_pos: int, max_pos: int, value: float, min_value: float, max_value: float, y_pos: int) -> None:
        """ 
        Initializes a slider object. 
        Args:
        slider_type (str): The type of the slider.
        min_pos (int): The x value for the minimum point of the slider.
        max_pos (int): The x value for the maximum point of the slider.
        value (float): The initial value of the slider.
        min_value (float): The minimum value of the slider.
        max_value (float): The maximum value of the slider.
        y_pos (int): The y position of the slider.
        """
        self.slider_type: str = slider_type
        self.font: pg.font.Font = pg.font.SysFont("Comicsans", 23)
        self.render_text()
        self.half_text_height: int = self.text.get_height() // 2
        self.image: pg.Surface = pg.Surface((17, 32))
        self.image.fill("white")
        pg.draw.rect(self.image, "black", (2, 2, 13, 28))
        self.min_pos: int = min_pos
        self.max_pos: int = max_pos    
        self.value: float = value
        self.min_value: float = min_value
        self.max_value: float = max_value  
        self.range: int = self.max_pos - self.min_pos
        value_in_percent: float = (self.value - self.min_value) / (self.max_value - self.min_value)
        self.pos: list[int] = [self.min_pos + self.range * value_in_percent, y_pos]      
        self.rect: pg.rect = self.image.get_rect(center=self.pos)
        self.outer_slider_path: tuple[int] = (self.min_pos - 2, y_pos - 5, self.range + 4, 10)
        self.inner_slider_path: tuple[int] = (self.min_pos, y_pos - 3, self.range, 6)
        self.collided: bool = False

    def render_text(self) -> None:
        """ Renders the text for the slider. """
        text_to_render: str = self.slider_type
        self.text_shadow: pg.Surface = self.font.render(text_to_render, True, "black")
        self.text: pg.Surface = self.font.render(text_to_render, True, "white")

    def check_collision(self) -> bool:
        """ Checks if the slider has been clicked and handles the sliding mechanism. """
        mouse_pos: tuple[int] = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.collided = True

        if pg.mouse.get_pressed()[0] and self.collided:
            self.pos[0] = mouse_pos[0]

            if self.pos[0] < self.min_pos:
                self.pos[0] = self.min_pos
            if self.pos[0] > self.max_pos:
                self.pos[0] = self.max_pos

            self.rect.center = self.pos

            self.value = (self.pos[0] - self.min_pos) / self.range * self.max_value
            return True

        if not pg.mouse.get_pressed()[0] and self.collided:
            self.collided = False
            self.rect.center = self.pos

    def get_value(self) -> float:
        """ Returns the current value of the slider. """
        return round(self.value, 2)

    def render(self, surf: pg.Surface) -> None:
        """
        Renders the slider on the given surface.
        Args:
        surf (pg.Surface): The surface to render the slider on.
        """
        pg.draw.rect(surf, "white", self.outer_slider_path)
        pg.draw.rect(surf, "black", self.inner_slider_path)
        surf.blit(self.image, self.rect)
        surf.blit(self.text_shadow, (self.max_pos + 30, self.pos[1] - self.half_text_height + 2))
        surf.blit(self.text, (self.max_pos + 32, self.pos[1] - self.half_text_height))
