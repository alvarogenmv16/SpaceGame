import pygame
import random

# Battle grid is a 3x3 matrix
GRID_ROWS = 3
GRID_COLS = 3
CELL_SIZE = 80
CELL_GAP = 10
CELL_BORDER_RADIUS = 8

DMG_PER_SHOT = 25

COLOR_UNKNOWN = (255, 255, 0)    # yellow
COLOR_HIT     = (255, 0, 0)      # red
COLOR_MISS    = (0, 255, 0)      # green
BORDER_COLOR  = (255, 255, 255)  # white
TEXT_COLOR    = (0, 0, 0)        # black

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
        
    def _cell_rect(self, row, col):
        x = self.origin_x + col * (CELL_SIZE + CELL_GAP)
        y = self.origin_y + row * (CELL_SIZE + CELL_GAP)
        return pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

    def fire(self, row, col):
        cell = self.grid[row][col]
        if cell["state"] != "unknown":
            return  # Already fired here

        if cell["compartment"] is not None:
            cell["compartment"].hp -= DMG_PER_SHOT
            cell["compartment"].hp = max(0, cell["compartment"].hp)
            cell["state"] = "hit"
        else:
            cell["state"] = "miss"

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS):
                    if self._cell_rect(row, col).collidepoint(event.pos):
                        self.fire(row, col)

    def draw(self, surface):
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                cell = self.grid[row][col]
                rect = self._cell_rect(row, col)

                if cell["state"] == "unknown":
                    color = COLOR_UNKNOWN
                    label = "?"
                elif cell["state"] == "hit":
                    color = COLOR_HIT
                    label = "X"
                else:
                    color = COLOR_MISS
                    label = "."

                pygame.draw.rect(surface, color, rect, border_radius=CELL_BORDER_RADIUS)
                pygame.draw.rect(surface, BORDER_COLOR, rect,
                                 width=2, border_radius=CELL_BORDER_RADIUS)

                text = self.font.render(label, True, TEXT_COLOR)
                surface.blit(text, (rect.centerx - text.get_width() // 2,
                                    rect.centery - text.get_height() // 2))