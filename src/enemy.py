import pygame
from compartment import Compartment, create_compartments
from battle_grid import BattleGrid

class EnemyShip:
    def __init__(self, screen_width, screen_height):
        self.x = 400
        self.y = 200
        self.sprite = pygame.image.load(r"../assets/enemy_sprite.png").convert_alpha()
        self.compartments = create_compartments(
            screen_width, screen_height, 
            ["Hull", "Engine", "Weapons", "Shields"], anchor="topleft")
        
        self.battle_grid = BattleGrid(pygame.Rect(0, 0, screen_width, screen_height), self.compartments)

    def update(self):
        pass

    def handle_event(self, event):
        self.battle_grid.handle_event(event)

    def draw(self, surface):
        self.battle_grid.draw(surface)
        rect = self.sprite.get_rect(center=(self.x, self.y))
        surface.blit(self.sprite, rect)        