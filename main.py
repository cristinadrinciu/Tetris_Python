import pygame, sys
from game import Game
from colors import Colors

from blocks import *

pygame.init()


# Create title font
title_font = pygame.font.SysFont("Arial", 30)

# Create the score surface
score_surface = title_font.render("Score" , True, Colors.white)

# Create the next surface (to display the next block)
next_surface = title_font.render("Next" , True, Colors.white)

# Create the game over surface
game_over_surface = title_font.render("Game Over", True, Colors.white)

# Create the button text surface
button_text = title_font.render("Switch", True, Colors.white)

# (x, y, width, height)
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
button = pygame.Rect(360, 500, 100, 60)

dayColor = (153, 204, 255)
nightColor = (0, 0, 0)

bgColor = dayColor

# Create the screen
screen = pygame.display.set_mode((495, 640))

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
            # Restart the game whenever a key on the keyboard is pressed
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        
        # Update movement every 200 ms only if the game is not over
        # Don't let the user move the block if the game is over
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if bgColor == dayColor:
                bgColor = nightColor
            else:
                bgColor = dayColor

    # Set background color
    screen.fill(bgColor)

    # Print score on screen
    screen.blit(score_surface, (365, 20, 50, 50))

    # Print next block on screen
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (328, 450, 60, 60))

    # Print 
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 100)
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, button, 0, 10)

    # Draw button text
    button_text_rect = button_text.get_rect(center=button.center)
    screen.blit(button_text, button_text_rect)

    game.draw(screen)
    
    # Update screen
    pygame.display.update()

    # 60 FPS - refresh rate
    clock.tick(60)
