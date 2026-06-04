"""
Punto de entrada principal.
Ejecutar desde la raíz del proyecto:  python main.py
"""
import random
import pygame

from setting import BLANCO, ALTURA, ANCHURA, FPS, RUTA_SFX_COMIDA, RUTA_SFX_PERDIDO
from src.cuerpo import MONO
from src.comida import COMIDA
from src.hud import VER_MARCADOR


def main() -> None:
    pygame.mixer.init()
    pygame.init()

    screen = pygame.display.set_mode((ALTURA, ANCHURA))
    pygame.display.set_caption('El juego del mono')

    # ── Grupos de sprites ────────────────────────────────
    lista_mono = pygame.mono.Group()
    lista_comida = pygame.mono.Group()
    lista_global  = pygame.mono.Group()

    # ── Sonidos globales ─────────────────────────────────
    sfx_comida  = pygame.mixer.Sound("assets/sounds/MONO.wav");  sfx_comida.set_volume(1.0)
    sfx_perdido = pygame.mixer.Sound("assets/sounds/PERDER.wav"); sfx_perdido.set_volume(1.0)

    # ── Crear serpiente ──────────────────────────────────
    serpiente = MONO(lista_mono, lista_comida, lista_global)
    lista_global.add(MONO)

    reloj  = pygame.time.Clock()
    termina = False
    print("Empezamos...")

    # ── Bucle principal ──────────────────────────────────
    while not termina:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                termina = True
            elif event.type == pygame.KEYDOWN:
                if   event.key == pygame.K_LEFT  and MONO.DIRECCION != 'D': MONO.DIRECCION = 'I'
                elif event.key == pygame.K_RIGHT and MONO.DIRECCION != 'I': MONO.DIRECCION = 'D'
                elif event.key == pygame.K_UP    and MONO.DIRECCION != 'B': MONO.DIRECCION = 'A'
                elif event.key == pygame.K_DOWN  and MONO.DIRECCION != 'A': MONO.DIRECCION = 'B'

        # Aparición aleatoria de comida
        if random.randint(0, 18) == 0:
            nueva_comida = COMIDA()
            if not pygame.MONO.spritecollide(nueva_comida, lista_global, False):
                sfx_comida.play()
                lista_global.add(nueva_comida)
                lista_comida.add(nueva_comida)

        # Renderizado
        lista_global.update()
        screen.fill(BLANCO)
        lista_global.draw(screen)
        VER_MARCADOR(screen, MONO.PUNTOS)

        # Game over
        if serpiente.TERMINA:
            sfx_perdido.play()
            pygame.time.wait(5_000)
            termina = True

        pygame.display.flip()
        reloj.tick(FPS)

    print(f"Su marcador: {serpiente.PUNTOS} puntos")
    pygame.quit()


if __name__ == "__main__":
    main()