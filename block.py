from colors import Colors
from position import Position
import pygame

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, row, columns):
        self.row_offset += row
        self.column_offset += columns

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    # create the rotate method for the block
    def rotate(self):
        # update rotation state
        self.rotation_state += 1

        # check if the rotation state has reached the maximum number of rotation states. If so, reset it
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    # create a method to undo rotation to use in case the block gets out of the grid during rotation
    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 15,
                                    tile.row * self.cell_size + 15,
                                    self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

