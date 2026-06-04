import pygame
import random
import os

class Comida:
    def __init__(self, largura_tela, altura_tela, tamanho_celula):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.tamanho_comida = 15
        self.velocidad = 3
        self.x = random.randint(0, largura_tela - self.tamanho_comida)
        self.y = 0
        self.ativo = True
        banana_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'banano.png')
        )
        self.imagen = pygame.image.load(banana_path).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (self.tamanho_comida, self.tamanho_comida))

    def mover(self):
        # La comida cae desde arriba
        self.y += self.velocidad
        
        # Si sale de la pantalla, crear nueva comida
        if self.y > self.altura_tela:
            self.ativo = False

    def gerar_posicao(self):
        x = random.randint(0, (self.largura_tela - self.tamanho_celula) // self.tamanho_celula) * self.tamanho_celula
        y = random.randint(0, (self.altura_tela - self.tamanho_celula) // self.tamanho_celula) * self.tamanho_celula
        return (x, y)

    def desenhar(self, tela):
        # Dibujar la comida usando la imagen de banana
        tela.blit(self.imagen, (self.x, self.y))
    
    def get_rect(self):
        # Retornar un rectángulo para detección de colisiones
        return pygame.Rect(self.x, self.y, self.tamanho_comida, self.tamanho_comida)
