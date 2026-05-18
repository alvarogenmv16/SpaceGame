import pygame
from compartment import Compartment

class PlayerShip:
    def __init__(self, screen_width, screen_height):
        self.x = 400
        self.y = 600
        self.sprite = pygame.image.load(r"../assets/player_sprite.png").convert_alpha()
        cw, ch = 150, 70
        gap = 12
        margin = 20

        x0 = screen_width - cw * 2 - gap - margin
        x1 = x0 + cw + gap

        y0 = screen_height - ch * 2 - gap - margin
        y1 = y0 + ch + gap

        self.compartments = [
            Compartment("Hull",    pygame.Rect(x0, y0, cw, ch)),
            Compartment("Engine",  pygame.Rect(x1, y0, cw, ch)),
            Compartment("Weapons", pygame.Rect(x0, y1, cw, ch)),
            Compartment("Shields", pygame.Rect(x1, y1, cw, ch)),
        ]

    def update(self):
        pass

    def handle_event(self, event):
        for c in self.compartments:
            c.handle_event(event)

    def draw(self, surface):
        rect = self.sprite.get_rect(center=(self.x, self.y))
        surface.blit(self.sprite, rect)
        for c in self.compartments:
            c.draw(surface)

