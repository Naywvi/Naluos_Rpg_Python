import time
from src.dialog import DialogBox
from src.healthbar import HealthBar
from src.map import Map, MapManager
from src.dead import DeathScreen
import pygame
import pytmx
import pyscroll

from src.player import Player

class Game:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Naluos - RPG Adventure !")
        self.clock = pygame.time.Clock()
        
        self.player = Player()
        
        self.health_bar = HealthBar(self.screen)
        self.death_screen = DeathScreen(self.screen)
        
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox(self.screen)
        self.dialog_inventory = DialogBox(self.screen)
        self.welcome_dialog_box = DialogBox(self.screen)
        
        self.welcome_dialog_box.reading = True
        self.delete_dialog_box = DialogBox(self.screen)
        self.welcome_dialog_box.texts = ["Coucou ! Appuie sur le boutton [H] 2 fois pour commencer !"]
        
    
    def update(self):
        self.map_manager.update()
    
    def run(self):
        running = True
        while running:
            
            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.health_bar.render(self.player.hp)
            self.dialog_box.render()
            self.welcome_dialog_box.render()
            self.dialog_inventory.render()
            if self.player.hp <= 0:
                self.death_screen.render()
                print(self.player.hp)
                self.player.hp-= 1
                if self.player.hp == -2:
                    self.map_manager.change_music("death")
                if self.player.hp <= -25:
                    pygame.quit()
            
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type ==  pygame.QUIT:
                    running = False
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_npc_collisions(self.dialog_box)
                    elif event.key == pygame.K_h:
                        self.map_manager.welcome_message(self.welcome_dialog_box)
                    elif event.key == pygame.K_f:
                        self.map_manager.delete_message(self.dialog_box)
                    elif event.key == pygame.K_e:
                        self.map_manager.inventory_message(self.dialog_inventory)
                        
                    
            self.clock.tick(20)
        
        pygame.quit()
    
    def handle_input(self):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]:
            self.player.move_up()
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
        elif pressed[pygame.K_LEFT]: 
            self.player.move_left()
        elif pressed[pygame.K_RIGHT]: 
            self.player.move_right()
        elif pressed[pygame.K_ESCAPE]:
            pygame.quit()
        #else: print("bouge pas")
        
        self.player.update()
