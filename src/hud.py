# Heads-Up Display (pantalla de información superpuesta)

import pygame
from setting import NEGRO, BLANCO, BALDOSA_TAMANIO, MARCADOR_ANCHURA, ALTURA


def VER_MARCADOR(screen, puntos: int) -> None:
    """Dibuja la barra de puntuación en la parte superior de la pantalla."""
    font       = pygame.font.SysFont('Arial', BALDOSA_TAMANIO - 5)
    background = pygame.Surface((ALTURA, MARCADOR_ANCHURA)).convert()
    background.fill(BLANCO)

    texto    = font.render(f"Puntos = {puntos}", True, NEGRO)
    textpos  = texto.get_rect(centerx=ALTURA / 2, centery=MARCADOR_ANCHURA / 2)
    background.blit(texto, textpos)
    screen.blit(background, (0, 0))