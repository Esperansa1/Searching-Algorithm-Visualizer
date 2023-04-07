from algorithm import Algorithm
import math
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)


class DFS(Algorithm):
    def __init__(self):
        super().__init__("DFS")
        self.open_set = []
        self.closed_set = []

    def initialize(self):
        super().initialize()

    def loop_algorithm(self):
        if len(self.open_set) == 0:
            self.run_simulation = False
            return
        self.color_sets()
        current_cell = self.open_set.pop()

        if current_cell == self.end_point:
            self.reconstruct_path()
            self.run_simulation = False

        if not current_cell.is_visited:
            current_cell.is_visited = True
            self.closed_set.append(current_cell)
            for neighbour in current_cell.neighbours:
                if neighbour.color == BLACK or neighbour.is_visited:
                    continue
                neighbour.parent = current_cell

                if neighbour == self.end_point:
                    self.reconstruct_path()
                    self.run_simulation = False
                else:
                    self.open_set.append(neighbour)

    def run_algorithm(self, start_point, end_point, grid):
        super().run_algorithm(start_point, end_point, grid)
        self.initialize()
        self.loop_algorithm()
