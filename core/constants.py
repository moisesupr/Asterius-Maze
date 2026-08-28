"""
Constantes del proyecto: colores, tamaños, estados
"""

#window
from enum import Enum


WIDTH = 500
HEIGHT = 400
TITLE = "Asterius Maze"
FPS = 60

#grid
CELL_SIZE = 40
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# Node States
class NodeState(Enum):
    EMPTY = 0
    WALL = 1
    START = 2
    END = 3
    VISITED = 4
    PATH = 5
    FRONTIER = 6

COLORS = {
    NodeState.EMPTY: (40, 40, 40),
    NodeState.WALL: (20, 20, 20),
    NodeState.START: (0, 200, 100),
    NodeState.END: (200, 50, 50),
    NodeState.VISITED: (100, 100, 180),
    NodeState.PATH: (255, 220, 50),
    NodeState.FRONTIER: (150, 150, 220),
}

# UI
BUTTON_COLOR = (70, 70, 70)
BUTTON_HOVER = (100, 100, 100)
TEXT_COLOR = (255, 255, 255)
