import pygame
from Algorithms.a_star import A_Star
from Algorithms.dijkstra import Dijkstra
from Algorithms.bfs import BFS
from Algorithms.dfs import DFS

from Algorithms.greedy_bfs import GreedyBFS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)


class AlgorithmManager:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.algorithms = [A_Star(),
                           Dijkstra(), BFS(), GreedyBFS(), DFS()]
        self.current_algorithm = self.algorithms[0]
        self.index = 0
        self.run_simulation = False

        self.weight_mode = False
        self.allow_diagonals = False

    def next_algorithm(self):
        self.index += 1
        if self.index == len(self.algorithms):
            self.index = 0
        self.current_algorithm = self.algorithms[self.index]
        self.run_simulation = False

    def draw_state(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(
            f'Algorithm: {self.current_algorithm.name}', True, BLACK)
        self.screen.blit(
            text, (self.width - 45 - text.get_width(), text.get_height() + 15))

        current_heuristic = self.current_algorithm.current_heuristic
        if current_heuristic != None:
            text = font.render(
                f'Heuristic: {self.current_algorithm.current_heuristic}', True, BLACK)
            self.screen.blit(
                text, (self.width - 45 - text.get_width(), text.get_height() + 55))

        mode = self.get_mode()
        text = font.render(mode, True, BLACK)
        self.screen.blit(text, (45, text.get_height() + 15))

        if self.allow_diagonals:
            text = font.render("Allow Diagonals", True, BLACK)
            self.screen.blit(
                text, (self.width - 45 - text.get_width(), text.get_height() + 90))

    def run_algorithm(self, start_point, end_point, grid):
        self.run_simulation = True
        self.current_algorithm.run_algorithm(start_point, end_point, grid)

    def loop_algorithm(self):
        self.run_simulation = self.current_algorithm.run_simulation
        self.current_algorithm.loop_algorithm()

    def get_mode(self):
        mode = "Running Simulation"
        if self.weight_mode and not self.run_simulation:
            mode = "Weight Mode"
        elif not self.weight_mode and not self.run_simulation:
            mode = "Wall Mode"
        return mode
