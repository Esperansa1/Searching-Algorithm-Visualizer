from cell import Cell
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class GridManager:
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.ROWS = 20

        self.CELL_WIDTH = WIDTH // self.ROWS
        self.CELL_HEIGHT = HEIGHT // self.ROWS

        self.grid = []
        self.initialize_grid()

    def initialize_grid(self):
        for i in range(self.ROWS):
            empty_grid = []
            for j in range(self.ROWS):
                empty_grid.append(Cell(i, j, WHITE))
            self.grid.append(empty_grid)

        for row in self.grid:
            for cell in row:
                cell.set_neighbours(self.grid)

    def draw_grid(self, screen):  # Draws grid lines
        for i in range(self.ROWS):
            pygame.draw.line(screen, BLACK, (i*self.CELL_WIDTH, 0),
                             (i*self.CELL_WIDTH, self.HEIGHT))
            pygame.draw.line(screen, BLACK, (0, i*self.CELL_HEIGHT),
                             (self.WIDTH, i*self.CELL_HEIGHT))

    def get_clicked_cell(self) -> Cell:
        """ Returns the cell clicked """
        x_mouse, y_mouse = pygame.mouse.get_pos()

        x_grid = x_mouse // self.CELL_WIDTH
        y_grid = y_mouse // self.CELL_HEIGHT

        if x_grid >= len(self.grid) or y_grid >= len(self.grid[0]) or x_grid < 0 or y_grid < 0:
            return None

        return self.grid[x_grid][y_grid]

    def draw_cells(self, screen):
        for row in self.grid:
            for cell in row:
                cell.draw(screen, self.CELL_WIDTH, self.CELL_HEIGHT)

    def draw(self, screen):
        self.draw_grid(screen)
        self.draw_cells(screen)

    def clear_weight_and_walls(self):
        for row in self.grid:
            for cell in row:
                if cell.color == BLACK or cell.weight > 1:
                    cell.weight = 1
                    cell.color = WHITE
