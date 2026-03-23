import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Es la clase que maneja las balas que dispara la nave"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Crea un rectangulo de bala en la posicion (0,0) 
        #y luego lo mueve a la posicion correcta
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Guarda la posicion de la bala con un valor decimal
        self.y = float(self.rect.y)


    def update(self):
        """Mueve la balla por la pantalla"""
        #Actualiza el valor decimal de la bala
        self.y -= self.settings.bullet_speed
        #Actualiza la pocision del rectangulo
        self.rect.y = self.y

    
    def draw_bullet(self):
        """Dibuja la bala en la pantalla"""
        pygame.draw.rect(self.screen, self.color, self.rect)