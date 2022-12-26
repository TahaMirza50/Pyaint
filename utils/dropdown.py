import pygame

class Dropdown:
    def __init__(self, x, y, width, height, font, options, name=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.options = options
        self.selected_option = options[0]
        self.expanded = False
        self.color = (200, 200, 200)
        self.option_height = self.font.size(options[0])[1]
        self.option_y = y + self.height
        self.name = name

    def draw(self, surface):
        # Draw the dropdown box
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

        # Draw the selected option text
        text = self.font.render(self.selected_option, True, (0, 0, 0))
        surface.blit(text, (self.x + 5, self.y + 5))

        # Draw the dropdown arrow
        pygame.draw.polygon(surface, (0, 0, 0), [(self.x + self.width - 15, self.y + self.height // 2),
                                                  (self.x + self.width - 5, self.y + self.height // 2 - 5),
                                                  (self.x + self.width - 5, self.y + self.height // 2 + 5)])
        if self.expanded:
            # Draw the options
            for i, option in enumerate(self.options):
                color = (200, 200, 200)
                if option == self.selected_option:
                    color = (255, 255, 255)
                pygame.draw.rect(surface, color, (self.x, self.option_y + i * self.option_height, self.width, self.option_height))
                text = self.font.render(option, True, (0, 0, 0))
                surface.blit(text, (self.x + 5, self.option_y + i * self.option_height + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the dropdown was clicked
            if self.x < event.pos[0] < self.x + self.width and self.y < event.pos[1] < self.y + self.height:
                self.expanded = not self.expanded
            # Check if an option was clicked
            elif self.expanded:
                for i, option in enumerate(self.options):
                    if self.x < event.pos[0] < self.x + self.width and self.option_y + i * self.option_height < event.pos[1] < self.option_y + (i+1) * self.option_height:
                        self.selected_option = option
                        self.expanded = False
                        break
            else:
                self.expanded = False
