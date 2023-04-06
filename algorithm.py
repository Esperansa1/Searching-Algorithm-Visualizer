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

    def color_sets(self):
        for cell in self.open_set:
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
                if cell.color != BLACK and cell.color != BLUE:
                    cell.color = WHITE

    def run_algorithm(self, start_point, end_point, grid):
        self.start_point = start_point
        self.end_point = end_point
        self.grid = grid
