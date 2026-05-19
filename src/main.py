import pygame
import sys
from player import PlayerShip
from enemy import EnemyShip

if __name__ == "__main__":
    pygame.init()
    # Window configuration
    screen_width, screen_height = 800, 800

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("SpaceGame")

    player_ship = PlayerShip(screen_width, screen_height)
    enemy_ship = EnemyShip(screen_width, screen_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((12, 18, 35))

        player_ship.update()
        player_ship.draw(screen)

        enemy_ship.update()
        enemy_ship.draw(screen)

        pygame.display.flip()
        clock.tick(60)