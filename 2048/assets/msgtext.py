import pygame
from assets.constants import FONTMESSAGE, WIDTH, HEIGHT

class BlinkText():
    def __init__(self, text):
        self.text = text
        self.timeChange = 0
        self.size = 18
        textSurface = FONTMESSAGE.render(self.text, False, (207,0,0))
        self.surface = pygame.Surface(textSurface.get_size())
        self.surface.fill((255, 255, 255))
        self.surface.set_colorkey((255, 255, 255))
        self.surface.blit(textSurface, (0, 0))
        self.alpha = 0

    def update(self):
        self.alpha = abs(int(255 - self.timeChange))
        if self.timeChange > 255*2:
            self.timeChange = 0
        self.timeChange += 5

    def draw(self, WIN):
        self.surface.set_alpha(self.alpha)
        WIN.blit(self.surface, (WIDTH // 2 - self.surface.get_width() // 2, HEIGHT // 2 - self.surface.get_height() // 2))