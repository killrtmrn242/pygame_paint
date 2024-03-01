import pygame
pygame.init()
pygame.font.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)
YELLOW = (255, 254, 32)
ORANGE = (255, 160, 16)
LIGHT_BLUE = (80, 208, 255)
PURPLE = (160, 32, 255)

FPS = 60

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

BRUSH_SIZE = 6
BRUSH_SIZE_MIN = 1
BRUSH_SIZE_MAX = 20
BRUSH_STROKE_SIZE = 5
DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("comicsans", size)