import pygame
import random

# Battle grid is a 3x3 matrix
GRID_ROWS = 3
GRID_COLS = 3
CELL_SIZE = 80
CELL_GAP = 10
CELL_BORDER_RADIUS = 8

DMG_PER_SHOT = 25

COLOR_UNKNOWN = (25, 50, 90)
COLOR_HIT     = (180, 60, 60)
COLOR_MISS    = (30, 60, 80)
BORDER_COLOR  = (90, 170, 255)
TEXT_COLOR    = (180, 220, 255)

class BattleGrid:
    def __init__(self, surface_rect, compartments):
        self.font = pygame.font.SysFont("consolas", 12, bold=True)

        # Centrar la cuadrícula en su área
        grid_w = GRID_COLS * CELL_SIZE + (GRID_COLS - 1) * CELL_GAP
        grid_h = GRID_ROWS * CELL_SIZE + (GRID_ROWS - 1) * CELL_GAP
        self.origin_x = surface_rect.centerx - grid_w // 2
        self.origin_y = surface_rect.centery - grid_h // 2

        # Initialize grid with "unknown" state and link to compartments
        self.grid = [[{"state": "unknown", "compartment": None}
                      for _ in range(GRID_COLS)]
                      for _ in range(GRID_ROWS)]

        # Arrange compartments randomly in the grid
        positions = random.sample(
            [(r, c) for r in range(GRID_ROWS) for c in range(GRID_COLS)],
            len(compartments)
        )
        for (row, col), compartment in zip(positions, compartments):
            self.grid[row][col]["compartment"] = compartment