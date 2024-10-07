# chessboard.py
import pygame
from chesspiece import Piece

class Chessboard:
    def __init__(self, screen):
        self.screen = screen
        self.board_size = 600
        self.square_size = self.board_size // 8
        self.colors = [pygame.Color(255, 206, 158), pygame.Color(209, 139, 71)]
        self.board = [[None] * 8 for _ in range(8)]
        
        # Load images once and store them in a dictionary
        self.piece_images = self.load_images()
        self.setup_pieces()

        self.selected_piece = None
        self.selected_square = None

    def load_images(self):
        # Dictionary to hold images, keyed by piece type and color
        images = {}
        for color in ['W', 'B']:
            for piece_type in ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']:
                # Load each image and store in the dictionary
                image = pygame.image.load(f'assets/{color}{piece_type}.png')
                # Resize if necessary
                images[f'{color}_{piece_type}'] = pygame.transform.scale(image, (self.square_size, self.square_size))
        return images

    def setup_pieces(self):
        # Using the dictionary to place pieces on the board
        for col in range(8):
            self.board[1][col] = Piece('pawn', 'B')
            self.board[6][col] = Piece('pawn', 'W')
        
        # Black pieces
        self.board[0][0] = Piece('rook', 'B')
        self.board[0][7] = Piece('rook', 'B')
        self.board[0][1] = Piece('knight', 'B')
        self.board[0][6] = Piece('knight', 'B')
        self.board[0][2] = Piece('bishop', 'B')
        self.board[0][5] = Piece('bishop', 'B')
        self.board[0][3] = Piece('queen', 'B')
        self.board[0][4] = Piece('king', 'B')

        # White pieces
        self.board[7][0] = Piece('rook', 'W')
        self.board[7][7] = Piece('rook', 'W')
        self.board[7][1] = Piece('knight', 'W')
        self.board[7][6] = Piece('knight', 'W')
        self.board[7][2] = Piece('bishop', 'W')
        self.board[7][5] = Piece('bishop', 'W')
        self.board[7][3] = Piece('queen', 'W')
        self.board[7][4] = Piece('king', 'W')
        # Add other pieces as needed

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = self.colors[(row + col) % 2]
                pygame.draw.rect(self.screen, color, pygame.Rect(col * self.square_size, row * self.square_size, self.square_size, self.square_size))

    def draw_pieces(self):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    # Use the image from the dictionary based on piece type and color
                    piece_image = self.piece_images[f'{piece.color}_{piece.type}']
                    self.screen.blit(piece_image, (col * self.square_size, row * self.square_size))
    
    # Function to ascertain piece coordinates and move if fits logic
    # Each square of the 8X8 is either None or a Piece object
    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos # separate the position into a tuple, one for column and one for row
        end_row, end_col = end_pos
        piece = self.board[start_row][start_col] # Access the Piece object at that location if there is one, otherwise the position in the list should contain None.

        # Simple example: allow movement if destination square is empty
        if self.board[end_row][end_col] is None:
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = None
            return True
        return False
    
    def handle_click(self, row, col):
        if self.selected_piece:
            # Try to move the selected piece to the clicked square
            if self.move_piece(self.selected_square, (row, col)):
                self.selected_piece = None
                self.selected_square = None
            else:
                # If move is invalid, deselect
                self.selected_piece = None
                self.selected_square = None
        else:
            # Select a piece if one exists at the clicked square
            piece = self.board[row][col]
            if piece:
                self.selected_piece = piece
                self.selected_square = (row, col)


