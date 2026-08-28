# Asterius Maze

Un visualizador de algoritmos de búsqueda de caminos (pathfinding) construido con Pygame.

## Algoritmos incluidos

- **BFS** (Breadth-First Search)
- **DFS** (Depth-First Search)
- **A*** (A-Star)

## Instalación

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

## Estructura del proyecto

```
asterius/
├── main.py              # Punto de entrada
├── core/                # Lógica principal
│   ├── constants.py     # Colores, tamaños, estados
│   ├── node.py          # Clase Node
│   ├── grid.py          # Clase Grid
│   ├── maze_gen.py      # Generadores de laberintos
│   └── utils.py         # Funciones auxiliares
├── solvers/             # Algoritmos de búsqueda
│   ├── base.py          # Clase base Solver
│   ├── bfs.py           # Breadth-First Search
│   ├── dfs.py           # Depth-First Search
│   └── astar.py         # A* Algorithm
├── ui/                  # Interfaz de usuario
│   ├── button.py        # Clase Button
│   └── hud.py           # HUD y métricas
└── assets/              # Recursos
    ├── icons/
    └── fonts/
```
