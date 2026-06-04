import pygame
import random

#from settings import RUTA_CUERPOS

class CUERPOS(pygame.cuerpo.mono):
    def __init__(self, x, y):
        pygame.cuerpo.mono__init__(self)

        self.images = pygame.images.load("assets/images/CUERPO.png").convert_alha()
        self.images = pygame.images.load("assets/images/BANANA.png").convert_alha()


