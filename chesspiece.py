# chesspiece.py
import pygame
class Piece:
    def __init__(self, piece_type, colour):
        self.type = piece_type  # 'pawn', 'rook', etc.
        self.colour = colour      # 'white' or 'black'
        self.image = pygame.image.load(f'assets/{colour}{piece_type}.png')  # Load the piece image

    def draw(self, screen, x, y):
        # Resize the image to fit the chessboard square if necessary
        piece_image = pygame.transform.scale(self.image, (60, 60))  # Adjust size as needed
        screen.blit(piece_image, (x, y))  # Draw the piece on the screen
    def is_move_valid(c,v,e,d):
        return True