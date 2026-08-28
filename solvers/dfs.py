"""
Depth-First Search (DFS) - Búsqueda en profundidad
"""
from core.constants import NodeState
from collections import deque
import pygame
def trace_path(end_node):
    current = end_node.parent

    while current is not None and current.state != NodeState.START:
        current.state = NodeState.PATH
        current = current.parent

def dfs(grid, start):
    #initialization
    
    stack = [start]

    while len(stack) > 0:

        current = stack.pop()

        # Cuando encuentras el END:
        if current.state == NodeState.END:
            trace_path(current)  # Pintar el camino amarillo
            return True
        
        if current.state != NodeState.START:
            current.state = NodeState.VISITED

        # Cuando agregas vecinos, guardar parent:
        for n in grid.get_neighbors(current):
            # Filter
            if n.state == NodeState.EMPTY or n.state == NodeState.END:
                n.parent = current
                stack.append(n)
                if n.state != NodeState.END:
                    n.state = NodeState.FRONTIER
    return False




