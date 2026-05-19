import pygame

# Compartment class and helper function to create compartments for the player's ship
COMPARTMENT_GAP = 12
COMPARTMENT_MARGIN = 20
COMPARTMENT_BORDER_RADIUS = 8
COMPARTMENT_BORDER_WIDTH = 2

# Font configuration for compartment labels
FONT_NAME = "consolas"
FONT_SIZE = 14

# Colors for compartments
COLOR_ACTIVE = (60, 140, 220)
COLOR_INACTIVE = (25, 60, 110)
BORDER_COLOR = (90, 170, 255)
TEXT_COLOR = (180, 220, 255)

GRID_COLS = 2

class Compartment:
    def __init__(self, name, rect):
        self.name = name
        self.rect = rect
        self.active = False  # Compartment starts inactive
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE, bold=True)  # Font for compartment name

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
    
    def draw(self, surface):
        color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        pygame.draw.rect(surface, color, self.rect, border_radius=COMPARTMENT_BORDER_RADIUS)
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, width=COMPARTMENT_BORDER_WIDTH, border_radius=COMPARTMENT_BORDER_RADIUS)

        label = self.font.render(self.name, True, TEXT_COLOR)

        lx = self.rect.centerx - label.get_width() // 2
        ly = self.rect.centery - label.get_height() // 2

        surface.blit(label, (lx, ly))

# Function to fill the matrix for compartments
def create_compartments(screen_width, screen_height, names):
    c_width, c_height = 150, 70
    cols = 2
    rows = 2

    start_x = screen_width  - c_width * cols - COMPARTMENT_GAP * (cols - 1) - COMPARTMENT_MARGIN
    start_y = screen_height - c_height * rows - COMPARTMENT_GAP * (rows - 1) - COMPARTMENT_MARGIN

    compartments = []
    for i, name in enumerate(names):
        col = i % cols
        row = i // cols
        x = start_x + col * (c_width + COMPARTMENT_GAP)
        y = start_y + row * (c_height + COMPARTMENT_GAP)
        compartments.append(Compartment(name, pygame.Rect(x, y, c_width, c_height)))

    return compartments