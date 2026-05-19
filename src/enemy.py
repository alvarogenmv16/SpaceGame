import pygame
from compartment import Compartment, create_compartments

class EnemyShip:
    def __init__(self, screen_width, screen_height):
        self.x = 400
        self.y = 200
        self.sprite = pygame.image.load(r"../assets/enemy_sprite.png").convert_alpha()
        self.compartments = create_compartments(
            screen_width, screen_height, 
            ["Hull", "Engine", "Weapons", "Shields"], anchor="topleft")

    def update(self):
        pass

    def draw(self, surface):
        rect = self.sprite.get_rect(center=(self.x, self.y))
        surface.blit(self.sprite, rect)
        for c in self.compartments:
            c.draw(surface)