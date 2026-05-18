import pygame

class PlayerShip:
    def __init__(self):
        self.x = 400
        self.y = 600

        self.sprite = pygame.image.load(r"../assets/player_sprite.png").convert_alpha()

    def update(self):
        pass

    def draw(self, surface):
        rect = self.sprite.get_rect(center=(self.x, self.y))
        surface.blit(self.sprite, rect)
