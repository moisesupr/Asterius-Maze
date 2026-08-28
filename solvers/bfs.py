from core.constants import NodeState
from collections import deque
import pygame

"""
Breadth-First Search (BFS) - Búsqueda en anchura
"""
def trace_path(end_node):
    current = end_node.parent

    while current is not None and current.state != NodeState.START:
        current.state = NodeState.PATH
        current = current.parent

def bfs(grid, start):
    #necessary queue
    q = deque()

    #inicializator / START NODE
    q.append(start)
    while len(q) > 0:

        current = q.popleft()

        # Cuando encuentras el END:
        if current.state == NodeState.END:
            trace_path(current)  # Pintar el camino amarillo
            return True
        
        if current.state != NodeState.START:
            current.state = NodeState.VISITED

        # Cuando agregas vecinos, guardar parent:
        for n in grid.get_neighbors(current):
            # Filtering
            if n.state == NodeState.EMPTY or n.state == NodeState.END:
                #making the way back making current the parent of n
                n.parent = current
                #adding n to the queue to keep going with him
                q.append(n)
                if n.state != NodeState.END:
                    n.state = NodeState.FRONTIER
                    
    return False




