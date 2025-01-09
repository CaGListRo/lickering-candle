import pygame as pg
import os
from typing import Final, TypeVar


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