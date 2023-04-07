
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)


class Algorithm:
    def __init__(self, name):
        self.name = name
        self.run_simulation = False
        self.start_point = None
        self.end_point = None

        self.open_set = []
        self.closed_set = []

        self.heuristic_index = 0
        self.heuristic_options = []
        self.current_heuristic = None

    def color_sets(self):
        for cell in self.open_set:
            if cell.color != PINK:
                cell.color = GREEN
        for cell in self.closed_set:
            if cell.color != PINK:
                cell.color = RED
        self.start_point.color = BLUE
        self.end_point.color = BLUE

    def reconstruct_path(self):
        current = self.end_point
        while current != self.start_point:
            current.color = PINK
            current = current.parent

    def initialize(self):
        self.closed_set = []
        self.open_set = [self.start_point]
        self.run_simulation = True

        for row in self.grid:
            for cell in row:
                cell.is_visited = False
                cell.parent = None
                cell.g = float('inf')
                if cell.color != BLACK and cell.color != BLUE:
                    cell.color = WHITE

        heuristic_function = self.manhattan_dist
        if self.current_heuristic == "Euclidean":
            heuristic_function = self.euclidean_dist
        elif self.current_heuristic == "Octile":
            heuristic_function = self.octile_dist
        elif self.current_heuristic == "Chebyshev":
            heuristic_function = self.chebyshev

        self.initialize_h_scores(heuristic_function)
        self.initialize_f_scores()

    def run_algorithm(self, start_point, end_point, grid):
        self.start_point = start_point
        self.end_point = end_point
        self.grid = grid

    def is_goal(self, cell):
        if cell == self.end_point:
            self.reconstruct_path()
            self.run_simulation = False

    def is_finished(self):
        if len(self.open_set) == 0:
            self.run_simulation = False
            return True
        return False

    def initialize_h_scores(self, heuristic_function):
        for row in self.grid:
            for cell in row:
                cell.h = heuristic_function(cell, self.end_point)

    def initialize_f_scores(self):
        for row in self.grid:
            for cell in row:
                cell.calculate_f_score()

    def next_heuristic_option(self):
        if len(self.heuristic_options) == 0:
            return
        self.heuristic_index += 1
        if self.heuristic_index == len(self.heuristic_options):
            self.heuristic_index = 0
        self.current_heuristic = self.heuristic_options[self.heuristic_index]
        self.run_simulation = False

    def get_distances(self, cell1, cell2):
        return cell1.i - cell2.i, cell1.j - cell2.j

    def manhattan_dist(self, cell1, cell2):
        dx, dy = self.get_distances(cell1, cell2)
        return abs(dx) + abs(dy)

    def euclidean_dist(self, cell1, cell2):  # Can also you the math.dist function
        dx, dy = self.get_distances(cell1, cell2)
        # can also use ** 0.5 instead of sqrt
        return math.sqrt(dx ** 2 + dy ** 2)

    def octile_dist(self, cell1, cell2):
        dx, dy = self.get_distances(cell1, cell2)
        f = math.sqrt(2) - 1
        if dx < dy:
            return f * dx + dy
        return f * dy + dx

    def chebyshev(self, cell1, cell2):
        dx, dy = self.get_distances(cell1, cell2)
        return max(dx, dy)
