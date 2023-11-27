import pygame

class Grid:
    def __init__(self):
        # set number of rows and cols
        self.num_rows = 20
        self.num_cols = 10

        # set cell size
        self.cell_size = 30

        # initialize list of colors
        self.colors = self.get_cell_colors()

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

    def get_cell_colors(self):
        gray = (32, 32, 32)
        magenta = (255, 0, 127)
        orange = (255, 128, 0)
        lila = (153, 153, 255)
        yellow = (255, 255, 0)
        light_green = (102, 255, 102)
        deep_green = (0, 153, 0)
        intense_red = (255, 0, 0)

        return [gray, magenta, orange, lila, yellow, light_green, deep_green, intense_red]

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]

                # draw the pixel square, which is going to be invisible, as it only represents a guide for the game pieces
                cell_rect = pygame.Rect(column * self.cell_size + 1, row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
                
                # call draw API
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

