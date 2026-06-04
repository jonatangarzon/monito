import os
import sys
import pygame
import random
from crs.mono import mono as MonoClass
from crs.comida import Comida

WIDTH, HEIGHT = 800, 600
CELL = 30
SPAWN_MS = 800
FPS = 60

# Colores disponibles para el jugador/fondo overlay
COLOR_OPTIONS = [
    (180, 180, 180),  # gris
    (255, 200, 0),    # amarillo
    (200, 50, 50),    # rojo
    (50, 150, 250),   # azul
    (50, 200, 100),   # verde
]

def main():
    pygame.init()
    try:
        pygame.mixer.init()
    except Exception:
        pass

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Monito")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    # Crear jugador; si falla usar fallback
    try:
        player = MonoClass(WIDTH, HEIGHT, CELL)
    except Exception:
        class FallbackPlayer:
            def __init__(self, w, h, cell):
                self.largura_tela = w
                self.altura_tela = h
                self.tamanho_mono = 30
                self.x = (w // 2) - (self.tamanho_mono // 2)
                self.y = h - self.tamanho_mono - 10
                self.velocidad = 5
                self.direccion = 0
                self.imagen = None
            def mover(self):
                self.x += self.direccion * self.velocidad
                if self.x < 0: self.x = 0
                if self.x + self.tamanho_mono > self.largura_tela:
                    self.x = self.largura_tela - self.tamanho_mono
            def desenhar(self, tela, color=(180,180,180), use_image=False):
                pygame.draw.rect(tela, color, (self.x, self.y, self.tamanho_mono, self.tamanho_mono))
        player = FallbackPlayer(WIDTH, HEIGHT, CELL)

    foods = []
    score = 0
    lives = 6
    color_idx = 0
    use_image_for_player = True
    game_over = False

    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, SPAWN_MS)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == SPAWN_EVENT and not game_over:
                foods.append(Comida(WIDTH, HEIGHT, CELL))

            elif event.type == pygame.KEYDOWN:
                # mover vidas con teclado + / - (también flechas)
                if event.key in (pygame.K_PLUS, pygame.K_KP_PLUS, pygame.K_UP):
                    lives += 1
                elif event.key in (pygame.K_MINUS, pygame.K_KP_MINUS, pygame.K_DOWN):
                    lives = max(0, lives - 1)
                # cambiar color con 'c'
                elif event.key == pygame.K_c:
                    color_idx = (color_idx + 1) % len(COLOR_OPTIONS)
                # alternar uso de imagen del mono con 'v'
                elif event.key == pygame.K_v:
                    use_image_for_player = not use_image_for_player
                # resetar con 'r'
                elif event.key == pygame.K_r:
                    foods.clear()
                    score = 0
                    lives = 7
                    game_over = False
                # establecer vidas directas con teclas 1-9
                elif pygame.K_1 <= event.key <= pygame.K_9:
                    lives = event.key - pygame.K_0

        keys = pygame.key.get_pressed()
        if not game_over:
            if keys[pygame.K_LEFT]:
                player.direccion = -1
            elif keys[pygame.K_RIGHT]:
                player.direccion = 1
            else:
                player.direccion = 0
        else:
            player.direccion = 0

        # Update
        try:
            player.mover()
        except Exception:
            pass

        # Mover comidas y detectar si llegan al suelo (perder vida)
        for f in foods:
            if hasattr(f, "mover"):
                try:
                    f.mover()
                except Exception:
                    f.y += getattr(f, "velocidad", 3)
            else:
                f.y += getattr(f, "velocidad", 3)

        # Colisión, pérdidas de vida y limpieza
        remaining = []
        for f in foods:
            rect_f = pygame.Rect(getattr(f, "x", 0), getattr(f, "y", 0),
                                 getattr(f, "tamanho_comida", 15), getattr(f, "tamanho_comida", 15))
            rect_p = pygame.Rect(getattr(player, "x", 0), getattr(player, "y", 0),
                                 getattr(player, "tamanho_mono", 30), getattr(player, "tamanho_mono", 30))

            # 1. Caso de colisión: el jugador la atrapa
            if rect_f.colliderect(rect_p):
                score += 1
                if getattr(f, "sonido", None):
                    try:
                        f.sonido.play()
                    except Exception:
                        pass
                # NO se agrega a remaining, por lo que desaparece
                continue

            # 2. Caso de caída al suelo: pasa del fondo
            if f.y > HEIGHT:
                if not game_over:
                    lives -= 1
                # NO se agrega a remaining, garantizando que se elimine y no vuelva a restar vidas
                continue

            # 3. Si no colisionó ni cayó al suelo, sigue en juego
            remaining.append(f)
            
        foods = remaining

        if lives <= 0:
            lives = 0
            game_over = True

        # Draw
        screen.fill((50, 150, 50))
        for f in foods:
            img = getattr(f, "imagen", None)
            if img:
                screen.blit(img, (f.x, f.y))
            else:
                pygame.draw.rect(screen, (255, 255, 0), (f.x, f.y, getattr(f, "tamanho_comida", 15), getattr(f, "tamanho_comida", 15)))

        # dibujar jugador: si tiene imagen y use_image_for_player True, usarla; si no, usar color
        player_color = COLOR_OPTIONS[color_idx]
        try:
            if use_image_for_player and getattr(player, "imagen", None):
                # dibuja imagen
                player.desenhar(screen)
                # opcional: dibujar contorno del color para visual feedback
                pygame.draw.rect(screen, player_color, (player.x, player.y, player.tamanho_mono, player.tamanho_mono), 2)
            else:
                # si la clase tiene desenhar que acepta color, usarla; sino dibujar rect
                try:
                    player.desenhar(screen, color=player_color, use_image=False)
                except TypeError:
                    pygame.draw.rect(screen, player_color, (player.x, player.y, getattr(player, "tamanho_mono", 30), getattr(player, "tamanho_mono", 30)))
                except Exception:
                    pygame.draw.rect(screen, player_color, (player.x, player.y, getattr(player, "tamanho_mono", 30), getattr(player, "tamanho_mono", 30)))
        except Exception:
            pygame.draw.rect(screen, player_color, (player.x, player.y, getattr(player, "tamanho_mono", 30), getattr(player, "tamanho_mono", 30)))

        # HUD
        txt = font.render(f"Puntos: {score}   Vidas: {lives}   Color: {color_idx+1}/{len(COLOR_OPTIONS)}   ImagenJugador: {'ON' if use_image_for_player else 'OFF'}", True, (255, 255, 255))
        screen.blit(txt, (10, 10))

        if game_over:
            go_txt = font.render("GAME OVER - Presiona R para reiniciar", True, (255, 50, 50))
            screen.blit(go_txt, (WIDTH//2 - go_txt.get_width()//2, HEIGHT//2 - 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()