from algorithm import Algorithm
import math
BLACK = (0, 0, 0)


class GreedyBFS(Algorithm):
    def __init__(self):
        super().__init__("Greedy BFS")
        self.open_set = []
        self.closed_set = []

    def initialize(self):
        super().initialize()
        for row in self.grid:
            for cell in row:
                cell.parent = None
                cell.h = float('inf')
        self.initialize_h_scores()
        self.start_point.h = 0

    def initialize_h_scores(self):
        for row in self.grid:
            for cell in row:
                cell.h = math.dist(
                    (cell.i, cell.j), (self.end_point.i, self.end_point.j))  # Euclidan

    def get_closest_cell(self):
        best_cell = self.open_set[0]
        for cell in self.open_set:
            if cell.h < best_cell.h:
                best_cell = cell
        return best_cell

    def loop_algorithm(self):
        if len(self.open_set) == 0:
            self.run_simulation = False
            return

        self.color_sets()
        current_cell = self.get_closest_cell()
        self.open_set.remove(current_cell)
        self.closed_set.append(current_cell)

        for neighbour in current_cell.neighbours:
            if neighbour.color == BLACK or neighbour in self.closed_set:
                continue
            if neighbour.parent == None:
                if neighbour == self.end_point:
                    neighbour.parent = current_cell
                    self.reconstruct_path()
                    self.run_simulation = False
                else:
                    self.open_set.append(neighbour)
                    neighbour.parent = current_cell

    def run_algorithm(self, start_point, end_point, grid):
        super().run_algorithm(start_point, end_point, grid)
        self.initialize()
        self.loop_algorithm()
