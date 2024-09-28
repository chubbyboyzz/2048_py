import pygame

pygame.init()

WIDTH = 300
HEIGHT = 300
SIZE_SQUARE = 75
BORDER = 2
SIZE_BLOCK = 4

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

ICON = pygame.image.load("./img/Apps-2048-icon.png")
BG = pygame.image.load("./img/2048_logo.png")
FPS = 60

FONT = pygame.font.SysFont('consolas', 30)
FONTMESSAGE = pygame.font.SysFont('consolas', 18)
