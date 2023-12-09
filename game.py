from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
    
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        
        # Update current block
        self.current_block = self.next_block

        # Generate new next block
        self.next_block = self.get_random_block()

        # Clear the full rows, if they are full and move the rest down 
        self.grid.clear_full_rows()
        
        # Check if the new block fits in the grid
        if self.block_fits() == False:
            # If the new block doesn't fit, we need to end the game
            self.game_over = True

    # Reset method to restart the game
    def reset(self):
        # Clear the grid
        self.grid.reset()

        # When the game ends, we need to select a new random current_block and a new next block from the list of blocks
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        #Select a random block to be the current block
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()


    # Check for collision of two or more blocks
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()

        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False

        return True

    def move_left(self):
        self.current_block.move(0, -1)

        # Check if block is inside the grid or if it fits (for collision)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)
    
    def move_right(self):
        self.current_block.move(0, 1)

        # Check if block is inside the grid
        if self.block_inside() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)

        #  Check if block is inside the grid or if it fits (for collision)
        if(self.block_inside() == False or self.block_fits() == False):
            self.current_block.move(-1, 0)
            # If block is at bottom, lock it.
            self.lock_block()

    def rotate(self):
        self.current_block.rotate()

        # Check if the block gets out of the grid during rotation and if it fits
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()

    def block_inside(self):

        # Get the tiles of the current block
        tiles = self.current_block.get_cell_positions()

        # Check if all tiles are inside the grid
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
