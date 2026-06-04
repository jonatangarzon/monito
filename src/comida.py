import pygame
import random

from setting import (
    BALDOSA_TAMANIO, BALDOSA_NUMERO, MARCADOR_ANCHURA, 
    DURACION_COMIDA_DESAPARECE,SUELO, RUTA_COMIDA,
)


class COMIDA(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("assets/images/COMIDA.png").convert_alpha()
        self.rect  = self.image.get_rect()

        self.rect.x = random.randint(0, BALDOSA_NUMERO - 1) * BALDOSA_TAMANIO
        self.rect.y = (random.randint(0, BALDOSA_NUMERO - 1) * BALDOSA_TAMANIO
                       + MARCADOR_ANCHURA)

        self.time = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.time > DURACION_COMIDA_DESAPARECE:
            self.kill()