import pygame
from chesspiece import Piece
class Pawn(Piece):
    def __init__(self, colour):
        super().__init__("pawn", colour)
    def is_move_valid(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Direction based on colour
        direction = -1 if self.colour == 'W' else 1
        # Move one square forward - returns True if square is empty (is None) and False if not
        if end_col == start_col and end_row == start_row + direction:
            return board[end_row][end_col] is None
        # Initial two-square move
        if end_col == start_col and end_row == start_row + 2 * direction:
            initial_row = 6 if self.colour == 'W' else 1 # initial = 6 if white otherwise 1. This is a hard coded coordinate, might need to make it dynamic if implementing features like flipping the board later.
            if start_row == initial_row and board[end_row][end_col] is None:
                return board[start_row + direction][start_col] is None
        # Capture diagonally
        # Check for whether the change in column is +- 1 AND the change in row is +- 1 depending on colour.
        if abs(end_col - start_col) == 1 and end_row == start_row + direction:
            # If there is a piece in that position, return true if it is a piece of the opposite colour, false otherwise
            if board[end_row][end_col] is not None:
                return board[end_row][end_col].colour != self.colour

        return False
