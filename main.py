from board import Board
import pygame, sys

# general setup
pygame.init()
clock = pygame.time.Clock()

# colors
BG_COLOR = (250, 250, 250)

# screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')
board = Board(screen, screen_width, screen_height)

def bg():
    block_size = 50
    GRAY = (245, 245, 245)
    for x in range(0, screen_width, block_size):
        for y in range(0, screen_height, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, GRAY, rect, 5)

# loop
while True:
    # events
    for event in pygame.event.get():
        # close window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)
    bg()

    board.run()

    pygame.display.update()
    clock.tick(60)