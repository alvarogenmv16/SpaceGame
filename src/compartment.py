import pygame

class Compartment:
    def __init__(self, name, rect):
        self.name = name
        self.rect = rect
        self.active = False  # Compartment starts inactive
        self.font = pygame.font.SysFont("consolas", 14, bold=True)  # Font for compartment name

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
    
    def draw(self, surface):
        if self.active:
            color = (60, 140, 220)
        else:
            color = (25, 60, 110)

        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        pygame.draw.rect(
            surface,
            (90, 170, 255),
            self.rect,
            width=2,
            border_radius=8
        )

        label = self.font.render(self.name, True, (180, 220, 255))

        lx = self.rect.centerx - label.get_width() // 2
        ly = self.rect.centery - label.get_height() // 2

        surface.blit(label, (lx, ly))