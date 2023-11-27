import pygame, sys
from grid import Grid

pygame.init()
bgColor = (153, 204, 255)

# Create the screen
screen = pygame.display.set_mode((300, 600))

pygame.display.set_caption("Python Tetris")

# Initialize clock
clock = pygame.time.Clock()

game_grid = Grid()


game_grid.grid[0][0] = 1
game_grid.grid[3][5] = 4
game_grid.grid[17][8] = 7


game_grid.display_matrix()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Set background color
    screen.fill(bgColor)

    game_grid.draw(screen)


    # Update screen
    pygame.display.update()

    # 60 FPS - refresh rate
    clock.tick(60)