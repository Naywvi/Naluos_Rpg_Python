from mimetypes import init
import pygame

class DialogBox:
    
    
    def __init__(self, screen, y = -10) -> None:
    
        self.screen = screen
        self.X_POSITION = self.screen.get_rect().center[0] / 2
        if y == -10: self.Y_POSITION = self.screen.get_rect().center[1] * 2 - 150
        else: self.Y_POSITION = y
        self.box = pygame.image.load("./assets/dialogs/dialog_box.png")
        self.box = pygame.transform.scale(self.box, (900,100))
        self.texts = []
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font("./assets/dialogs/dialog_font.ttf", 18)
        self.reading = False
        self.render_y = 0
        
    def render(self):
        if self.reading:
            
            if len(self.texts) > 0:
                if len(self.texts[0]) >= 0:
                    if self.letter_index >= len(self.texts[self.text_index]):
                        self.letter_index = self.letter_index
                    self.letter_index += 1
                    self.screen.blit(self.box, (self.X_POSITION-100, self.Y_POSITION))
                    text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0,0,0))
                    self.screen.blit(text, (self.X_POSITION-30, self.Y_POSITION + 38))
                    
    
    def execute(self, dialog=[]):
        if self.reading:
            self.next_text()
        else:
            self.reading = True
            self.text_index = 0
            self.texts = dialog
    
    def next_text(self):
        self.letter_index = 0
        self.text_index += 1
        
        if self.text_index >= len(self.texts):
            self.reading = False
        