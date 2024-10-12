import pygame
from chesspiece import Piece

class Rook(Piece):
    def __init__(self, piece_type, colour):
        super().__init__(piece_type, colour)

    def is_move_valid(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Rook must move either in a straight line vertically or horizontally
        if start_row != end_row and start_col != end_col:
            return False  # Not a valid Rook move (not in a straight line)

        # Determine the direction of movement
        row_step = 0
        col_step = 0
        if start_row == end_row:
            col_step = 1 if end_col > start_col else -1
        elif start_col == end_col:
            row_step = 1 if end_row > start_row else -1

        # Check each square along the path, stopping before the last square
        current_row, current_col = start_row + row_step, start_col + col_step
        while current_row != end_row or current_col != end_col:
            if board[current_row][current_col] is not None:
                return False  # A piece is blocking the path
            current_row += row_step
            current_col += col_step

        # Final square check: must be either empty or occupied by an opponent piece
        if board[end_row][end_col] is None or board[end_row][end_col].colour != self.colour:
            return True

        return False
