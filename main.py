import sys
import pygame
from cell import Cell
from a_star import A_Star
from algorithm_manager import AlgorithmManager

# Color RGB Codes

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)

# Initialize Pygame

pygame.init()
pygame.display.set_caption("Serach Algorithms")
fps = 60
clock = pygame.time.Clock()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))


start_point = None
end_point = None

ROWS = 20
CELL_WIDTH = WIDTH // ROWS
CELL_HEIGHT = HEIGHT // ROWS
grid = []

# Search algorithms options
a_star = A_Star()


# Manages the information appearing on screen and cycling algorithms
algorithm_manager = AlgorithmManager(screen, WIDTH, HEIGHT)


# Initializing the 2 dimensional grid
def initialize_grid():
    global start_point, end_point
    for i in range(ROWS):
        empty_grid = []
        for j in range(ROWS):
            empty_grid.append(Cell(i, j, WHITE))
        grid.append(empty_grid)

    for row in grid:
        for cell in row:
            cell.set_neighbours(grid)
    # start_point = grid[1][1]
    # end_point = grid[49][49]


def draw_grid():
    """
    Draws the grid lines
    Return: None
    """
    for i in range(ROWS):
        pygame.draw.line(screen, BLACK, (i*CELL_WIDTH, 0),
                         (i*CELL_WIDTH, HEIGHT))
        pygame.draw.line(screen, BLACK, (0, i*CELL_HEIGHT),
                         (WIDTH, i*CELL_HEIGHT))


def get_cell_clicked() -> Cell:
    """ Returns the cell clicked """
    x_mouse, y_mouse = pygame.mouse.get_pos()

    x_grid = x_mouse // CELL_WIDTH
    y_grid = y_mouse // CELL_HEIGHT

    return grid[x_grid][y_grid]


def draw_cells():
    for row in grid:
        for cell in row:
            cell.draw(screen, CELL_WIDTH, CELL_HEIGHT)


def on_click(cell, click):
    global start_point, end_point

    if click[0]:  # If left click is pressed
        if start_point != None and end_point != None and cell != end_point and cell != start_point:
            cell.color = BLACK

        if start_point == None:
            start_point = cell
            start_point.color = BLUE
        elif end_point == None and cell != start_point:
            end_point = cell
            end_point.color = BLUE

    elif click[2]:  # If right click is pressed
        cell.color = WHITE
        if cell == start_point:
            start_point = None
        elif cell == end_point:
            end_point = None

    # Game loop.


initialize_grid()

start_simulation = False

open_set = []
closed_set = []


while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        click = pygame.mouse.get_pressed()
        if (click[0] or click[2]) and algorithm_manager.run_simulation == False:
            cell = get_cell_clicked()
            on_click(cell, click)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if start_point != None and end_point != None:
                    algorithm_manager.run_algorithm(
                        start_point, end_point, grid)
            # if event.key == pygame.K_n:
            #     if start_point != None and end_point != None:
            #         algorithm_manager.loop_algorithm()

            if event.key == pygame.K_p:
                algorithm_manager.next_algorithm()

    if algorithm_manager.run_simulation:
        algorithm_manager.loop_algorithm()

    draw_grid()
    draw_cells()
    algorithm_manager.draw_state()

    pygame.display.update()
    clock.tick(fps)
