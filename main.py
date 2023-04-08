import sys
import pygame
from algorithm_manager import AlgorithmManager
from grid_manager import GridManager


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

# Draws and manages the grid
grid_manager = GridManager(WIDTH, HEIGHT)

algorithm_manager = AlgorithmManager(screen, WIDTH, HEIGHT)


def on_click(cell, click):
    global start_point, end_point

    if click[0]:  # If left click is pressed
        if algorithm_manager.weight_mode and cell.color != BLUE:
            cell.weight += 1
            return

        if start_point != None and end_point != None and cell != end_point and cell != start_point:
            cell.color = BLACK

        if start_point == None:
            start_point = cell
            start_point.weight = 1
            start_point.color = BLUE
        elif end_point == None and cell != start_point:
            end_point = cell
            end_point.weight = 1
            end_point.color = BLUE

    elif click[2]:  # If right click is pressed
        if algorithm_manager.weight_mode and cell.color != BLUE:
            if cell.weight > 1:
                cell.weight -= 1
                return
        cell.color = WHITE
        if cell == start_point:
            start_point = None
        elif cell == end_point:
            end_point = None


def handle_key_press(event):
    if event.key == pygame.K_SPACE:
        if start_point != None and end_point != None:
            algorithm_manager.run_algorithm(
                start_point, end_point, grid_manager.grid)

    elif event.key == pygame.K_p:
        algorithm_manager.next_algorithm()

    elif event.key == pygame.K_w:
        algorithm_manager.weight_mode = not algorithm_manager.weight_mode

    elif not algorithm_manager.run_simulation:
        if event.key == pygame.K_c:
            grid_manager.clear_weight_and_walls()

        elif event.key == pygame.K_n:
            algorithm_manager.current_algorithm.next_heuristic_option()

        elif event.key == pygame.K_u:
            algorithm_manager.allow_diagonals = not algorithm_manager.allow_diagonals
            grid_manager.update_neighbours(algorithm_manager.allow_diagonals)


while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        click = pygame.mouse.get_pressed()
        if (click[0] or click[2]) and not algorithm_manager.run_simulation:
            cell = grid_manager.get_clicked_cell()
            if cell != None:
                on_click(cell, click)

        if event.type == pygame.KEYDOWN:
            handle_key_press(event)

    if algorithm_manager.run_simulation:
        algorithm_manager.loop_algorithm()

    grid_manager.draw(screen)
    algorithm_manager.draw_state()

    pygame.display.update()
    clock.tick(fps)
