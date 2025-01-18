### Flickering Candle Simulation

This project is a Python-based simulation of a flickering candle. The simulation includes adjustable sliders for controlling various parameters such as flicker speed, transparency, and background color.

## Features

Realistic candle flickering effect.
Adjustable sliders to control:

- Minimum flicker interval.
- Maximum flicker interval.
- Candle transparency.
- Background brightness.
- Dynamically loaded images for flame animations.
- FPS display in the window caption.

## Requirements

Python 3.8 or higher.
pygame library.

## Installation

Clone this repository or download the files.
Ensure pygame is installed:
pip install pygame

Place all required images for the flame animation in the images/ directory.

## Usage

Run the main script:
python main.py

Use the sliders at the bottom of the window to adjust the simulation:
MIN: Adjust the minimum flicker interval.
MAX: Adjust the maximum flicker interval.
DIM: Adjust the transparency of the flame.
BGRD: Adjust the background brightness.

## File Descriptions

main.py
The main script that initializes the simulation. It handles:

- Creating the game window.
- Loading images for the flame animation.
- Managing sliders for user input.
- Rendering the candle and background.
- Updating the display and handling user events.

utils.py
Contains utility functions and classes:

- load_image: Loads a single image and prepares it for rendering.
- load_images: Loads all images in a directory for the flame animation.
- Slider: A class for creating and managing sliders to adjust simulation parameters.

## Directory Structure

project/
├── images/
│ ├── flame1.png
│ ├── flame2.png
│ └── ...
├── main.py
├── utils.py
└── README.md

## Notes

Ensure the images/ directory is in the same location as the scripts.
Image files for the flame animation should be named consistently and sorted correctly to ensure smooth animation.

## License

This project is open source and available under the MIT License.
