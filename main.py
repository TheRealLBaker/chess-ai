# main.py
import pygame
from chessboard import Chessboard
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Chess Game")
clock = pygame.time.Clock()

# Create chessboard instance
chessboard = Chessboard(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle the piece selection and movement
            x, y = pygame.mouse.get_pos()
            # Adjust for border thickness on both sides before calculating row and col
            # This accounts for the top and left borders
            adjusted_x = x - chessboard.border_thickness
            adjusted_y = y - chessboard.border_thickness

            # Check if click is within the bounds of the 8*8 chessboard
            # This condition accounts for values outside of the grid, i.e., right and bottom borders
            if 0 <= adjusted_x < chessboard.square_size * 8 and 0 <= adjusted_y < chessboard.square_size * 8:
                # Calculate row and col within the board grid
                row = adjusted_y // chessboard.square_size
                col = adjusted_x // chessboard.square_size
                chessboard.handle_click(row, col)  # Handle the click in the chessboard class

    # Draw everything
    chessboard.draw_board()
    chessboard.draw_pieces()  # Call this method later once pieces are added

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Set the frame rate

pygame.quit()