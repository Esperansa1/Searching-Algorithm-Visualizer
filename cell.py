import pygame
BLACK = (0, 0, 0)


class Cell:
    def __init__(self, i, j, color):
        self.i = i
        self.j = j

        self.weight = 1

        self.color = color
        self.parent = None
        self.is_visited = False

        self.neighbours = []

        self.h = float('inf')
        self.g = float('inf')
        self.f = float('inf')

        self.font = pygame.font.Font('freesansbold.ttf', 18)

    def __repr__(self) -> str:
        return f"{self.i}, {self.j}"

    def draw(self, screen, cell_width, cell_height):
        pygame.draw.rect(screen, self.color, (self.i*cell_width+1,
                         self.j * cell_height+1, cell_width-1, cell_height-1))
        if self.weight != 1:
            self.draw_weight(screen, cell_width, cell_height)

    def draw_weight(self, screen, cell_width, cell_height):
        weight = self.font.render(
            f'{self.weight - 1}', True, BLACK)

        screen.blit(weight, (self.i * cell_width +
                    cell_width // 2, self.j * cell_height + cell_height // 2))

    def set_neighbours(self, grid):
        try:
            if self.i+1 < len(grid):
                self.neighbours.append(grid[self.i+1][self.j])

            if self.i - 1 >= 0:
                self.neighbours.append(grid[self.i-1][self.j])

            if self.j + 1 < len(grid[0]):
                self.neighbours.append(grid[self.i][self.j + 1])

            if self.j - 1 >= 0:
                self.neighbours.append(grid[self.i][self.j - 1])
        except:
            pass

    def calculate_f_score(self):
        self.f = self.h + self.g
