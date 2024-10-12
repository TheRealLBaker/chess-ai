import pygame
from chesspiece import Piece

class Bishop(Piece):
    def __init__(self, piece_type, colour):
        super().__init__(piece_type, colour)
    def is_move_valid(self, start_pos, end_pos, board):
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
    

def get_legal_moves(self, start_row, start_col, board):
        legal_moves = []
        # Define all four diagonal directions
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        # Iterate over each direction
        for row_step, col_step in directions:
            current_row, current_col = start_row + row_step, start_col + col_step

            # Continue moving in the current direction until you hit a boundary or another piece
            while 0 <= current_row < 8 and 0 <= current_col < 8:
                if board[current_row][current_col] is None:
                    # If the square is empty, it's a valid move
                    legal_moves.append((current_row, current_col))
                elif board[current_row][current_col].color != self.color:
                    # If there's an opponent piece, add the move, then break to stop in this direction
                    legal_moves.append((current_row, current_col))
                    break
                else:
                    # If there's a friendly piece, stop in this direction
                    break

                # Move to the next square in this direction
                current_row += row_step
                current_col += col_step

        return legal_moves
