import pygame, sys
from game import Game

from blocks import *

pygame.init()
bgColor = (153, 204, 255)

# Create the screen
screen = pygame.display.set_mode((300, 600))

pygame.display.set_caption("Python Tetris")

# Initialize clock
clock = pygame.time.Clock()

# Initialize game object
game = Game()

# Create timer event (to update more frequently)
GAME_UPDATE = pygame.USEREVENT

# Trigger game update event every 200 ms
pygame.time.set_timer(GAME_UPDATE, 200)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Add the input controls here
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP:
                game.rotate()
        
        # Update movement every 200 ms
        if event.type == GAME_UPDATE:
            game.move_down()

    # Set background color
    screen.fill(bgColor)
    game.draw(screen)
    
    # Update screen
    pygame.display.update()

    # 60 FPS - refresh rate
    clock.tick(60)
