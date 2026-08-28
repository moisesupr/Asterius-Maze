import pygame
import random
from solvers.bfs import bfs
from solvers.dfs import dfs
from core.grid import Grid
from core.constants import NodeState, ROWS, COLS

#important functions
def clicked_pos(pos):
    x, y = pos
    row = y // grid.cell_size #divided to get the position of the grid
    col = x // grid.cell_size
    return row, col

def randomizeLaberinth():
    #end bool so there is no more than one end
    end_exists = False
    for row in range(grid.rows):
        for col in range(grid.cols):
            node = grid.get_node(row, col)
            #center predefined start
            if row == grid.rows//2 and col == grid.cols//2:
                node.state = NodeState.START
            #end on a board 
            if col == grid.cols-1 and end_exists == False and random.randint(0, 5) == 0:
                node.state = NodeState.END
                end_exists = True
            if row == grid.rows//2 and col == grid.cols//2:
                node.state = NodeState.START
            elif random.randint(0, 5) == 0:
                node.state = NodeState.WALL
            elif random.randint(0, 5) == 2:
                node.state = NodeState.EMPTY

    return 0

def clean():
    for row in range(grid.rows):
        for col in range(grid.cols):
            node = grid.get_node(row, col)
            node.state = NodeState.EMPTY
            node.parent = None  # ← Resetear el parent también
    return 0
# Initialization
pygame.init()

# window
WIDTH = 500
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asterius Maze")

# FPS clock
clock = pygame.time.Clock()

# Crear el grid
grid = Grid(rows=ROWS, cols=COLS)  # Usar constantes

# principal loop
running = True
while running:
    # CLICK EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Toggle walls on click
        if event.type == pygame.MOUSEBUTTONDOWN:
            row, col = clicked_pos(event.pos)
            node = grid.get_node(row, col)
            #toggle wall state
            if node.state == NodeState.EMPTY:
                node.state = NodeState.WALL
            elif node.state == NodeState.WALL:
                node.state = NodeState.EMPTY
        
        # start, end, reset with keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                print("s presionada")
                if node.state == NodeState.START:
                    node.state = NodeState.EMPTY
                elif node.state == NodeState.EMPTY:
                    node.state = NodeState.START
            if event.key == pygame.K_e:
                print("e presionada")
                if node.state == NodeState.END:
                    node.state = NodeState.EMPTY
                elif node.state == NodeState.EMPTY:
                    node.state = NodeState.END
                    
        #randomize laberinth
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print("r presionada")
                randomizeLaberinth()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("space presionada")
                bfs(grid, grid.get_node(ROWS//2, COLS//2))  # Usar constantes para el nodo de inicio
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                dfs(grid, grid.get_node(ROWS//2, COLS//2))
        #clean laberinth
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                clean()
        



    # Dibujar fondo (gris)
    screen.fill('black')
    
    # Dibujar grid
    grid.draw(screen)
    
    # Actualizar pantalla
    pygame.display.flip()
    
    # 60 FPS
    clock.tick(60)

pygame.quit()
