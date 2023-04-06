from algorithm import Algorithm
import math
BLACK = (0, 0, 0)  # Wall color
WHITE = (255, 255, 255)  # Empty cell color
RED = (255, 0, 0)  # Closed set color
GREEN = (0, 255, 0)  # Open set color
BLUE = (0, 0, 255)  # Start and end point colors
PINK = (255, 192, 203)  # Path color


class Dijkstra(Algorithm):
    def __init__(self):
        super().__init__("Dijkstra")
        self.open_set = []
        self.closed_set = []

    def initialize(self):
        super().initialize()
        for row in self.grid:
            for cell in row:
                cell.h = float('inf')
        self.start_point.h = 0

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
        cell = self.get_closest_cell()

        if cell == self.end_point:
            self.reconstruct_path()
            self.run_simulation = False

        self.open_set.remove(cell)
        self.closed_set.append(cell)

        for neighbour in cell.neighbours:
            if neighbour.color == BLACK or neighbour in self.closed_set:
                continue
            temp_distance = cell.h + 1

            if temp_distance < neighbour.h:
                neighbour.h = temp_distance
                neighbour.parent = cell
                if neighbour not in self.open_set:
                    self.open_set.append(neighbour)

    def run_algorithm(self, start_point, end_point, grid):
        super().run_algorithm(start_point, end_point, grid)
        self.initialize()
        self.loop_algorithm()
