import pygame
BLACK = (0, 0, 0)


class Cell:
    def __init__(self, i, j, color):
        self.i = i
        self.j = j
        self.color = color
        self.parent = None
        self.neighbours = []
        self.h = float('inf')
        self.g = float('inf')
        self.f = float('inf')
        self.font = pygame.font.Font('freesansbold.ttf', 10)

    def __repr__(self) -> str:
        return f"{self.i}, {self.j}"

    def draw(self, screen, cell_width, cell_height):
        pygame.draw.rect(screen, self.color, (self.i*cell_width+1,
                         self.j * cell_height+1, cell_width-1, cell_height-1))
        # self.draw_values(screen, cell_width, cell_height)

    def draw_values(self, screen, cell_width, cell_height):
        text1 = self.font.render(
            f'H: {self.h}', True, BLACK)
        text2 = self.font.render(
            f'G: {self.g}', True, BLACK)
        text3 = self.font.render(
            f'F: {self.f}', True, BLACK)
        screen.blit(text1, (self.i * cell_width, self.j * cell_height))
        screen.blit(text2, (self.i * cell_width, self.j * cell_height+10))
        screen.blit(text3, (self.i * cell_width, self.j * cell_height+20))

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
