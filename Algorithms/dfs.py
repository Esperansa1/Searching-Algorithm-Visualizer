from algorithm import Algorithm

BLACK = (0, 0, 0)


class DFS(Algorithm):
    def __init__(self):
        super().__init__("DFS")

    def loop_algorithm(self):
        if self.is_finished():
            return

        self.color_sets()
        current_cell = self.open_set.pop()

        self.is_goal(current_cell)
        self.closed_set.append(current_cell)
        for neighbour in current_cell.neighbours:
            if neighbour.color == BLACK or neighbour.is_visited:
                continue

            neighbour.parent = current_cell
            neighbour.is_visited = True

            if neighbour == self.end_point:
                self.reconstruct_path()
                self.run_simulation = False
            else:
                self.open_set.append(neighbour)

    def run_algorithm(self, start_point, end_point, grid):
        super().run_algorithm(start_point, end_point, grid)
        self.initialize()
        self.loop_algorithm()
