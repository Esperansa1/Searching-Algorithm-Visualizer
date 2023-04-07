from algorithm import Algorithm
BLACK = (0, 0, 0)  # Wall color


class Dijkstra(Algorithm):
    def __init__(self):
        super().__init__("Dijkstra")

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
        if self.is_finished():
            return

        self.color_sets()
        cuurent_cell = self.get_closest_cell()
        self.is_goal(cuurent_cell)

        self.open_set.remove(cuurent_cell)
        self.closed_set.append(cuurent_cell)

        for neighbour in cuurent_cell.neighbours:
            if neighbour.color == BLACK or neighbour.is_visited:
                continue
            temp_distance = cuurent_cell.h + neighbour.weight

            if temp_distance < neighbour.h:
                neighbour.h = temp_distance
                neighbour.parent = cuurent_cell
                if neighbour not in self.open_set:
                    self.open_set.append(neighbour)

    def run_algorithm(self, start_point, end_point, grid):
        super().run_algorithm(start_point, end_point, grid)
        self.initialize()
        self.loop_algorithm()
