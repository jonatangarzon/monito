import pygame
import random
import os

# ...existing code...
class Comida:
    def __init__(self, largura_tela, altura_tela, tamanho_celula):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.tamanho_comida = 15
        self.velocidad = 5
        self.tamanho_celula = tamanho_celula
        self.x = random.randint(0, max(0, largura_tela - self.tamanho_comida))
        self.y = 0
        self.ativo = True

        # Cargar imagen (banano.png) o cualquier imagen disponible en assets/images
        assets_img_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'images'))
        banana_path = os.path.join(assets_img_dir, 'banano.png')
        self.imagen = None
        if os.path.exists(banana_path):
            try:
                self.imagen = pygame.image.load(banana_path).convert_alpha()
            except Exception:
                self.imagen = None
        if not self.imagen and os.path.isdir(assets_img_dir):
            for f in os.listdir(assets_img_dir):
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    try:
                        self.imagen = pygame.image.load(os.path.join(assets_img_dir, f)).convert_alpha()
                        break
                    except Exception:
                        self.imagen = None
        if self.imagen:
            self.imagen = pygame.transform.scale(self.imagen, (self.tamanho_comida, self.tamanho_comida))
        else:
            # Fallback si no se encuentra la imagen
            surf = pygame.Surface((self.tamanho_comida, self.tamanho_comida), pygame.SRCALPHA)
            surf.fill((255, 255, 0, 255))
            self.imagen = surf

        # Cargar sonido opcional
        self.sonido = None
        sounds_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'sounds'))
        if os.path.isdir(sounds_dir):
            for f in os.listdir(sounds_dir):
                if f.lower().endswith(('.wav', '.ogg', '.mp3')):
                    try:
                        if not pygame.mixer.get_init():
                            try:
                                pygame.mixer.init()
                            except Exception:
                                pass
                        if pygame.mixer.get_init():
                            self.sonido = pygame.mixer.Sound(os.path.join(sounds_dir, f))
                        break
                    except Exception:
                        self.sonido = None
# ...existing code...