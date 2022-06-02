import pygame

class HealthBar:
    
    def __init__(self, screen) -> None:
        self.screen = screen
        self.X_POS = 0
        self.Y_POS = self.screen.get_rect().center[1] * 2 - 60
        self.width = 60
        self.height = 50
        self.box = pygame.image.load("./assets/imgSprite/heart.png")
        self.box = pygame.transform.scale(self.box, (self.width, self.height))
        
    def render(self, hp_number):
        for i in range(0, hp_number):
            x = i * self.width
            self.screen.blit(self.box, (x + self.X_POS, self.Y_POS))
