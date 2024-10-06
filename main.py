# main.py
import pygame
from chessboard import Chessboard
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Chess Game")
clock = pygame.time.Clock()

# Create chessboard instance
chessboard = Chessboard(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw everything
    chessboard.draw_board()
    chessboard.draw_pieces()  # Call this method later once pieces are added

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Set the frame rate

pygame.quit()