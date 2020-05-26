import os


# Note we don't keep any images here, just configuration options
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BG_COLOR = (230, 230, 230)
BULLET_COLOR = (0, 0, 255)

# we'll setup our directory structure here because this file is in the top level of our project
ROOT_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(ROOT_DIR, 'images')
IMAGES_BG_DIR = os.path.join(IMAGES_DIR, 'background')
IMAGES_PE_DIR = os.path.join(IMAGES_DIR, 'player-enemies')