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

# Colors for HP bars
COLOR_HP_HIGH     = (60, 140, 220)   # >60%
COLOR_HP_MED      = (220, 140, 40)   # 30-60%
COLOR_HP_LOW      = (220, 60, 60)    # <30%
COLOR_HP_BG       = (20, 30, 50)

HP_BAR_HEIGHT  = 8
HP_BAR_MARGIN  = 8

class Compartment:
    MAX_HP = 100
    def __init__(self, name, rect):
        self.name = name
        self.rect = rect
        self.hp = self.MAX_HP
        self.active = False  # Compartment starts inactive
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE, bold=True)  # Font for compartment name

    def _bar_color(self):
        if self.hp > 60:
            return COLOR_HP_HIGH
        elif self.hp > 30:
            return COLOR_HP_MED
        else:
            return COLOR_HP_LOW
        
    def _draw_hp_bar(self, surface):
        bar_x = self.rect.x      + HP_BAR_MARGIN
        bar_y = self.rect.bottom - HP_BAR_MARGIN - HP_BAR_HEIGHT
        bar_w = self.rect.width  - HP_BAR_MARGIN * 2

        pygame.draw.rect(surface, COLOR_HP_BG,
                         pygame.Rect(bar_x, bar_y, bar_w, HP_BAR_HEIGHT),
                         border_radius=4)
        
        fill_w = int(bar_w * self.hp / self.MAX_HP)
        if fill_w > 0:
            pygame.draw.rect(surface, self._bar_color(),
                             pygame.Rect(bar_x, bar_y, fill_w, HP_BAR_HEIGHT),
                             border_radius=4)
    
    def draw(self, surface):
        color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        pygame.draw.rect(surface, color, self.rect, border_radius=COMPARTMENT_BORDER_RADIUS)
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, width=COMPARTMENT_BORDER_WIDTH, border_radius=COMPARTMENT_BORDER_RADIUS)

        label = self.font.render(self.name, True, TEXT_COLOR)

        lx = self.rect.centerx - label.get_width() // 2
        ly = self.rect.centery - label.get_height() // 2

        surface.blit(label, (lx, ly))

        self._draw_hp_bar(surface)

# Function to fill the matrix for compartments
def create_compartments(screen_width, screen_height, names, anchor="bottomright"):
    c_width, c_height = 150, 70
    cols = 2
    rows = 2

    if anchor == "bottomright":
        start_x = screen_width  - c_width * cols - COMPARTMENT_GAP * (cols - 1) - COMPARTMENT_MARGIN
        start_y = screen_height - c_height * rows - COMPARTMENT_GAP * (rows - 1) - COMPARTMENT_MARGIN
    elif anchor == "topleft":
        start_x = COMPARTMENT_MARGIN
        start_y = COMPARTMENT_MARGIN

    compartments = []
    for i, name in enumerate(names):
        col = i % cols
        row = i // cols
        x = start_x + col * (c_width + COMPARTMENT_GAP)
        y = start_y + row * (c_height + COMPARTMENT_GAP)
        compartments.append(Compartment(name, pygame.Rect(x, y, c_width, c_height)))

    return compartments