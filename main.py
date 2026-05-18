import pygame
import sys

# Initialize pygame
if __name__ == "__main__":
    pygame.init()
    # Window configuration
    screen_width = 800
    screen_hight = 800
    screen = pygame.display.set_mode((screen_width, screen_hight))
    clock = pygame.time.Clock()

    pygame.display.set_caption("SpaceGame")

    # Main Game loop
    while True:

    # Events
        for event in pygame.event.get():

        # Close window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit

        # Fill background
        screen.fill((30,30,30))

        # Update screen
        pygame.display.flip()

        # Limit FPS
        clock.tick(60)