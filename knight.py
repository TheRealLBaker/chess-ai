import pygame
from chesspiece import Piece

class Knight(Piece):
    def __init__(self, piece_type, colour):
        super().__init__(piece_type, colour)
    def is_move_valid(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Check for L-shape movement
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        if not ((row_diff == 1 and col_diff == 2) or (row_diff == 2 and col_diff == 1)):
            return False
        return True