import pygame
from a_star import A_Star
from dijkstra import Dijkstra
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
        self.algorithms = [A_Star(), Dijkstra()]
        self.current_algorithm = self.algorithms[0]
        self.index = 0
        self.run_simulation = False

    def next_algorithm(self):
        self.index += 1
        if self.index == len(self.algorithms):
            self.index = 0
        self.current_algorithm = self.algorithms[self.index]

    def draw_state(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(
            f'Current Algorithm: {self.current_algorithm.name}', True, BLACK)
        self.screen.blit(
            text, (self.width - 50 - text.get_width(), text.get_height() + 15))

    def run_algorithm(self, start_point, end_point, grid):
        self.run_simulation = True
        self.current_algorithm.run_algorithm(start_point, end_point, grid)

    def loop_algorithm(self):
        self.run_simulation = self.current_algorithm.run_simulation
        self.current_algorithm.loop_algorithm()
