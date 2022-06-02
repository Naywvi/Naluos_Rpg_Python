from email.mime import image
import pygame

class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, name, sprite_y_positions = {'up' : 48, 'right' : 32,'down' : 0,'left' : 16 }, starting_sprite_x = 0, step = 16, number_of_sprite_x = 3, image_sprite_size = 16) -> None:
        super().__init__()
        self.image_sprite_size = image_sprite_size
        self.starting_sprite_x = starting_sprite_x
        self.number_of_sprite_x = number_of_sprite_x
        self.walk_speed = 3.5
        self.clock = 0
        self.imageWidth = step
        self.animation_index = 0
        self.sprite_sheet = pygame.image.load(f'./assets/imgSprite/{name}.png')
        self.images = {
            'up': self.get_images(sprite_y_positions['up']),
            'left': self.get_images(sprite_y_positions['left']),
            'right': self.get_images(sprite_y_positions['right']),
            'down': self.get_images(sprite_y_positions['down']),
        }
    
    def change_animation(self, name): 
        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey([0,0,0])
        self.clock += self.walk_speed * 10
        
        if self.clock >= 100:
            self.animation_index += 1
            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0
            self.clock = 0
            
    def get_images(self, y):
        images = []
        for i in range(0, self.number_of_sprite_x):
            x = i*self.imageWidth + self.starting_sprite_x
            image = self.get_image(x, y)
            images.append(image)
        return images
        
    def get_image(self, x, y):
        image = pygame.Surface([self.image_sprite_size,self.image_sprite_size])
        image.blit(self.sprite_sheet, (0,0), (x, y, self.image_sprite_size, self.image_sprite_size))
        return image

    