import pygame
from chesspiece import Piece
class Queen(Piece):
    def __init__(self, piece_type, colour):
        super().__init__(piece_type, colour)

    # Checker function, see whether movement is valid (diagonal and vertical/horizontal)
    # Pass input into is_bishop_move_valid if diagonal movement
    # Pass input into is_rook_move_valid if vertical/horizontal movement.
    def is_move_valid(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Calculate row and column differences
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        # Queen can move like a Rook or a Bishop
        if row_diff == col_diff:
            # Diagonal move (Bishop's movement)
            return self.is_bishop_move_valid(start_pos, end_pos, board)
        elif row_diff == 0 or col_diff == 0:
            # Horizontal or vertical move (Rook's movement)
            return self.is_rook_move_valid(start_pos, end_pos, board)
        
        return False
    
    # Check whether diagonal movement restrictions are followed
    def is_bishop_move_valid(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Check for diagonal movement
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        if row_diff != col_diff:
            return False
        
        # Determine direction of movement
        row_step = 1 if end_row > start_row else -1
        col_step = 1 if end_col > start_col else -1
        

        # While loop to check for pieces blocking the diagonal
        # Check all squares along the path for obstructions
        current_row, current_col = start_row + row_step, start_col + col_step
        # Checks for all the squares up to one before the final square. If any piece obstructs the path
        # i.e., a not None square before the end sqaure, then false is returned to signify obstruction.
        while current_row != end_row and current_col != end_col:
            if board[current_row][current_col] is not None:
                return False
            current_row += row_step
            current_col += col_step

        # Check the final square for an opponent piece or empty space
        if board[end_row][end_col] is None or board[end_row][end_col].colour != self.colour:
            return True
        
        return False
    
    # Check whether rook-like movements are followed
    def is_rook_move_valid(self, start_pos, end_pos, board):
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
    