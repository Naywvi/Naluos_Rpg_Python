import sys
import pygame
from src.game import Game
pygame.init()

pygame.init()
 

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width = screen.get_rect().center[0] * 2
# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText
 
 
# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
 
# Game Fonts
font = "Retro.ttf"
 
 
# Game Framerate
clock = pygame.time.Clock()
FPS=30
# Main Menu
def main_menu(game):
 
    menu=True
    selected="start"
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        game.run()
                    if selected=="quit":
                        pygame.quit()
                        quit()
 
        # Main Menu UI
        screen.fill(blue)
        title=text_format("Naluos Adventure", font, 90, yellow)
        help=text_format("Pour la sélection, utilisez les flèches directionnelles ainsi que la touche entrée", font, 45, white)
        if selected=="start":
            text_start=text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)
 
        title_rect=title.get_rect()
        help_rect=help.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 500))
        screen.blit(help, (screen_width/2 - (help_rect[2]/2), 200))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Naluos - Adventure")

if __name__ == '__main__':
    pygame.init()
    game = Game()
    
    main_menu(game)
    #game.run()