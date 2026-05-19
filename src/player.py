import pygame
from compartment import Compartment, create_compartments

class PlayerShip:
    def __init__(self, screen_width, screen_height):
        self.x = 400
        self.y = 600
        self.sprite = pygame.image.load(r"../assets/player_sprite.png").convert_alpha()
        self.compartments = create_compartments(
            screen_width, screen_height, 
            ["Hull", "Engine", "Weapons", "Shields"])

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

