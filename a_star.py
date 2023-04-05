from algorithm import Algorithm
import math
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)


class A_Star(Algorithm):
    def __init__(self):
        super().__init__("A*")
        self.open_set = []
        self.closed_set = []

    def initialize(self):
        self.closed_set = []
        self.open_set = [self.start_point]
        self.run_simulation = True
        for row in self.grid:
            for cell in row:
                cell.g = float('inf')
                if cell.color != BLACK and cell.color != BLUE:
                    cell.color = WHITE
        self.start_point.g = 0
        self.initialize_h_scores()
        self.initialize_f_scores()

    def get_lowest_f_score(self):
        best_cell = self.open_set[0]
        for cell in self.open_set:
            if cell.f < best_cell.h:
                best_cell = cell
        return best_cell

    def initialize_h_scores(self):
        for row in self.grid:
            for cell in row:
                cell.h = math.dist(
                    (cell.i, cell.j), (self.end_point.i, self.end_point.j))  # Euclidan
                # cell.h = (cell.i - self.end_point.i) ** 2 + \
                #     (cell.j - self.end_point.j) ** 2

    def initialize_f_scores(self):
        for row in self.grid:
            for cell in row:
                cell.calculate_f_score()

    def color_sets(self):
        for cell in self.open_set:
            cell.color = GREEN
        for cell in self.closed_set:
            if cell.color != PINK:
                cell.color = RED

    def reconstruct_path(self):
        path = []
        current = self.end_point
        while current != self.start_point:
            path.append(current)
            current.color = PINK
            current = current.parent

    def loop_algorithm(self):
        if len(self.open_set) != 0:
            self.color_sets()
            current_cell = self.get_lowest_f_score()
            if current_cell == self.end_point:
                self.reconstruct_path()
                self.run_simulation = False

            self.open_set.remove(current_cell)
            self.closed_set.append(current_cell)

            for neighbour in current_cell.neighbours:
                if neighbour.color == BLACK or neighbour in self.closed_set:
                    continue

                tentantive_gScore = current_cell.g + 1
                if tentantive_gScore < neighbour.g:
                    neighbour.parent = current_cell
                    neighbour.g = tentantive_gScore
                    neighbour.f = tentantive_gScore + neighbour.h
                    if neighbour not in self.open_set:
                        self.open_set.append(neighbour)
        self.start_point.color = BLUE
        self.end_point.color = BLUE

    def run_algorithm(self, start_point, end_point, grid):
        self.start_point = start_point
        self.end_point = end_point
        self.grid = grid
        self.initialize()
        self.loop_algorithm()
