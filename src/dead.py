import pygame

class DeathScreen:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.X_POS = 0
        self.Y_POS = 0
        self.width = self.screen.get_rect().center[0] * 2
        self.height = self.screen.get_rect().center[1] * 2
        self.box = pygame.image.load("./assets/imgSprite/died.png")
        self.box = pygame.transform.scale(self.box, (self.width, self.height))
        
    def render(self):
        self.screen.blit(self.box, (self.X_POS, self.Y_POS))

        