# ── Colores ──────────────────────────────────────────────
NEGRO  = (0,   0,   0)
BLANCO = (255, 255, 255)

# ── Dimensiones ───────────────────────────────────────────
BALDOSA_TAMANIO   = 32
BALDOSA_NUMERO    = 15
MARCADOR_ANCHURA  = 32

ALTURA  = BALDOSA_TAMANIO * BALDOSA_NUMERO
ANCHURA = BALDOSA_TAMANIO * BALDOSA_NUMERO + MARCADOR_ANCHURA

# ── Juego ─────────────────────────────────────────────────
PUNTO_UNIDAD              = 1
DURACION_COMIDA_DESAPARECE = 5_500   # ms
FPS                       = 7

# ── Rutas de recursos (relativas a la raíz del proyecto) ──
import os

BASE_DIR    = os.path.join(os.path.dirname(__file__), "..", "assets")
RUTA_CABEZA  = os.path.join(BASE_DIR, "CABEZA.png")
RUTA_CUERPOS = os.path.join(BASE_DIR, "CUERPOS.png")
RUTA_COMIDA  = os.path.join(BASE_DIR, "COMIDA.png")
RUTA_SFX_COMIDA  = os.path.join(BASE_DIR, "COMIDA.wav")
RUTA_SFX_PERDIDO = os.path.join(BASE_DIR, "PERDIDO.wav")