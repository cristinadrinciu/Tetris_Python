import pygame, sys

pygame.init()
bgColor = (3, 151, 151)

# Create the screen
screen = pygame.display.set_mode((300, 600))

pygame.display.set_caption("Python Tetris")

# Initialize clock
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Set background color
    screen.fill(bgColor)
    # Update screen
    pygame.display.update()

    # 60 FPS - refresh rate
    clock.tick(60)