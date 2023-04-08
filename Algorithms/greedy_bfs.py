from algorithm import Algorithm

BLACK = (0, 0, 0)


class GreedyBFS(Algorithm):
    def __init__(self):
        super().__init__("Greedy BFS")

        self.heuristic_options = ["Manhattan",
                                  "Euclidean", "Octile", "Chebyshev"]
        self.current_heuristic = self.heuristic_options[0]

    def initialize(self):
        super().initialize()
        self.start_point.h = 0

    def get_closest_cell(self):
        best_cell = self.open_set[0]
        for cell in self.open_set:
            if cell.h < best_cell.h:
                best_cell = cell
        return best_cell

    def loop_algorithm(self):
        if self.is_finished():
            return

        self.color_sets()
        current_cell = self.get_closest_cell()
        self.open_set.remove(current_cell)
        self.closed_set.append(current_cell)

        for neighbour in current_cell.neighbours:
            if neighbour.color == BLACK or neighbour.is_visited:
                continue
            if not neighbour.is_visited:
                neighbour.parent = current_cell
                neighbour.is_visited = True
                if neighbour == self.end_point:

                    self.reconstruct_path()
                    self.run_simulation = False
                    return
                self.open_set.append(neighbour)

    def run_algorithm(self, start_point, end_point, grid):
        super().run_algorithm(start_point, end_point, grid)
        self.initialize()
        self.loop_algorithm()
