import pygame

class Text:
    def __init__(self, x, y, font, text='', color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.font = font
        self.text = text
        self.color = color

    def draw(self, surface):
        # Render the text
        text = self.font.render(self.text, True, self.color)
        # Blit the text on the screen
        surface.blit(text, (self.x, self.y))

