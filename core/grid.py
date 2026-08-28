#Clase Grid con matriz de nodos
from .node import Node
from .constants import CELL_SIZE

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cell_size = CELL_SIZE  # Guardar como atributo
        # Crear nodos automáticamente
        self.grid = [[Node(row, col, CELL_SIZE) for col in range(cols)] for row in range(rows)]
    
    #set node at position (row, col)
    def set_node(self, row, col, node):
        self.grid[row][col] = node

    #return node at position (row, col)
    def get_node(self, row, col):
        return self.grid[row][col]


    #print grid to console
    def display(self):
        for row in self.grid:
            print(" | ".join(str(node) if node is not None else "." for node in row))
    
    #this function returns a list with the nodes from up, down, left, right
    def get_neighbors(self, node):
        neighbors = []
        row = node.row
        col = node.col 
        # up
        if row > 0:
            neighbors.append(self.grid[row - 1][col])
        # down
        if row < self.rows - 1:
            neighbors.append(self.grid[row + 1][col])
        # left
        if col > 0:
            neighbors.append(self.grid[row][col - 1])
        
        # right
        if col < self.cols - 1:
            neighbors.append(self.grid[row][col + 1])
        
        return neighbors 
    #draw grid
    def draw(self, win):
        for row in self.grid:
            for node in row:
                if node is not None:
                    node.draw(win)
