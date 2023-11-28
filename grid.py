import pygame
from colors import Colors

class Grid:
    def __init__(self):
        # set number of rows and cols
        self.num_rows = 20
        self.num_cols = 10

        # set cell size
        self.cell_size = 30

        # initialize list of colors
        self.colors = Colors.get_cell_colors()

        # initialize grid (represented as a list of lists)
        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def display_matrix(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    def is_inside(self, row, column):
        if row < 0 or row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    # Check if a cell is empty
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]

                # draw the pixel square, which is going to be invisible, as it only represents a guide for the game pieces
                cell_rect = pygame.Rect(column * self.cell_size + 1, row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
                
                # call draw API
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

