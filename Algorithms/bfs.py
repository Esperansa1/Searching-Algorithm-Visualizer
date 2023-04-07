from algorithm import Algorithm
import math
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)


class BFS(Algorithm):
    def __init__(self):
        super().__init__("BFS")
        self.open_set = []
        self.closed_set = []

    def initialize(self):
        super().initialize()
        for row in self.grid:
            for cell in row:
                cell.parent = None

    def loop_algorithm(self):
        if len(self.open_set) == 0:
            self.run_simulation = False
            return

        self.color_sets()
        current_cell = self.open_set.pop(0)

        self.closed_set.append(current_cell)

        if current_cell == self.end_point:
            self.reconstruct_path()
            self.run_simulation = False

        for neighbour in current_cell.neighbours:
            if neighbour.color == BLACK or neighbour in self.closed_set:
                continue
            if not neighbour.is_visited:
                neighbour.is_visited = True
                self.open_set.append(neighbour)
                neighbour.parent = current_cell

    def run_algorithm(self, start_point, end_point, grid):
        super().run_algorithm(start_point, end_point, grid)
        self.initialize()
        self.loop_algorithm()
