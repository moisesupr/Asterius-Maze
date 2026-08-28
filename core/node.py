# Node class
import pygame
from .constants import NodeState, COLORS

class Node:
    def __init__(self, row, col, size):
        # POSICIÓN LÓGICA (grid)
        self.row = row          # y lógico
        self.col = col          # x lógico

        # POSICIÓN REAL (pixeles)
        self.x = col * size
        self.y = row * size
        self.size = size

        # ESTADO DEL ALGORITMO
        self.state = NodeState.EMPTY    # empty, open, closed, path, start, end

        # PARA RECONSTRUIR CAMINOS
        self.parent = None

    def draw(self, win):
        color = COLORS[self.state]
        pygame.draw.rect(win, color, (self.x, self.y, self.size - 1, self.size - 1))

