from algorithm import Algorithm

BLACK = (0, 0, 0)


class BFS(Algorithm):
    def __init__(self):
        super().__init__("BFS")

    def loop_algorithm(self):
        if self.is_finished():
            return

        self.color_sets()

        current_cell = self.open_set.pop(0)
        self.closed_set.append(current_cell)

        self.is_goal(current_cell)

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
