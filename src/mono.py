import os
import pygame

class mono:
    def __init__(self, largura_tela, altura_tela, tamanho_celula):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.tamanho_celula = tamanho_celula
        self.tamanho_mono = 30  # Tamaño del mono
        self.x = (largura_tela // 2) - (self.tamanho_mono // 2)  # Posición X centrada
        self.y = altura_tela - self.tamanho_mono - 10  # Cerca del fondo
        self.velocidad = 5
        self.direccion = 0  # -1: izquierda, 0: parado, 1: derecha
        
        ruta_imagen = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'mono.png')
        )
        self.imagen = pygame.image.load(ruta_imagen).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (self.tamanho_mono, self.tamanho_mono))

    def mover(self):
        # Mover según la dirección
        self.x += self.direccion * self.velocidad
        
        # Limitar a los bordes de la pantalla
        if self.x < 0:
            self.x = 0
        elif self.x + self.tamanho_mono > self.largura_tela:
            self.x = self.largura_tela - self.tamanho_mono

    def desenhar(self, tela):
        # Dibujar el mono usando la imagen mono.png
        tela.blit(self.imagen, (self.x, self.y))
