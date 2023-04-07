from algorithm import Algorithm

BLACK = (0, 0, 0)


class A_Star(Algorithm):
    def __init__(self):
        super().__init__("A*")

        self.heuristic_options = ["Manhattan",
                                  "Euclidean", "Octile", "Chebyshev"]
        self.current_heuristic = self.heuristic_options[0]

    def initialize(self):
        super().initialize()
        self.start_point.g = 0

    def get_lowest_f_score(self):
        best_cell = self.open_set[0]
        for cell in self.open_set:
            if cell.f < best_cell.f:
                best_cell = cell
        return best_cell

    def loop_algorithm(self):
        if self.is_finished():
            return

        self.color_sets()
        current_cell = self.get_lowest_f_score()
        self.is_goal(current_cell)

        self.open_set.remove(current_cell)
        self.closed_set.append(current_cell)
        current_cell.is_visited = True

        for neighbour in current_cell.neighbours:
            if neighbour.color == BLACK or neighbour.is_visited:
                continue

            tentantive_gScore = current_cell.g + neighbour.weight
            if tentantive_gScore < neighbour.g:
                neighbour.parent = current_cell
                neighbour.g = tentantive_gScore
                neighbour.f = tentantive_gScore + neighbour.h
                if neighbour not in self.open_set:
                    self.open_set.append(neighbour)

    def run_algorithm(self, start_point, end_point, grid):
        super().run_algorithm(start_point, end_point, grid)
        self.initialize()
        self.loop_algorithm()
