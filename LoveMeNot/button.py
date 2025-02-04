import pygame
from music_and_sound import button_click, button_hover

class Button:
    def __init__(self, x, y, width, height, text, font, base_color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.base_color = base_color
        self.hover_color = hover_color
        self.action = action
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.hovered = False

    def draw(self, surface):
        """Draws the button, using hover color if the mouse is over it."""
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse_pos)

        # Play hover sound only if the hover state just changed
        if is_hovered and not self.hovered:
            button_hover.play()
        self.hovered = is_hovered

        # Set button color based on hover state
        color = self.hover_color if self.hovered else self.base_color
        pygame.draw.rect(surface, color, self.rect)
        surface.blit(self.text_surface, self.text_rect)

    def handle_event(self, event):
        """Handles button clicks."""
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
            button_click.play()

            if self.action:
                self.action()
