# chessboard.py
import pygame
from chesspiece import Piece
from pawn import Pawn

class Chessboard:
    def __init__(self, screen):
        self.screen = screen
        self.board_size = 600
        self.square_size = self.board_size // 8
        self.colours = [pygame.Color(255, 206, 158), pygame.Color(209, 139, 71)]
        self.board = [[None] * 8 for _ in range(8)]
        
        # Load images once and store them in a dictionary
        self.piece_images = self.load_images()
        self.setup_pieces()

        self.selected_piece = None
        self.selected_square = None
        # Colour variables
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        # Set up the border color and thickness
        self.border_color = (0, 0, 0)  # Black border
        self.border_thickness = 50
    def load_images(self):
        # Dictionary to hold images, keyed by piece type and colour
        images = {}
        for colour in ['W', 'B']:
            for piece_type in ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']:
                # Load each image and store in the dictionary
                image = pygame.image.load(f'assets/{colour}{piece_type}.png')
                # Resize if necessary
                images[f'{colour}_{piece_type}'] = pygame.transform.scale(image, (self.square_size, self.square_size))
        return images

    def setup_pieces(self):
        # Using the dictionary to place pieces on the board
        for col in range(8):
            self.board[1][col] = Pawn('B')
            self.board[6][col] = Pawn('W')
        
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
         # Draw the border around the chessboard
        pygame.draw.rect(self.screen, self.border_color,
                        pygame.Rect(0, 0, self.square_size * 8, self.square_size * 8), self.border_thickness)

        # Draw the squares of the chessboard
        for row in range(8):
            for col in range(8):
                colour = self.colours[(row + col) % 2]  # Choose color based on position
                pygame.draw.rect(self.screen, colour, 
                                pygame.Rect(col * self.square_size + self.border_thickness, 
                                            row * self.square_size + self.border_thickness, 
                                            self.square_size, 
                                            self.square_size))
        
        # Draw labels for files (columns) and ranks (rows)
        font = pygame.font.Font(None, 36)
        # Draw file labels (a-h) at the top
        for col in range(8):
            file_label = chr(col + 97)  # Convert 0-7 to 'a'-'h'
            text = font.render(file_label, True, self.WHITE)  # Use WHITE for better visibility
            text_rect = text.get_rect(center=(col * self.square_size + self.square_size // 2 + self.border_thickness, 
                                                self.border_thickness // 2))  # Position above the board
            self.screen.blit(text, text_rect)

        # Draw rank labels (1-8) at the left side
        for row in range(8):
            rank_label = str(8 - row)  # Convert 0-7 to '1'-'8'
            text = font.render(rank_label, True, self.WHITE)  # Use WHITE for better visibility
            text_rect = text.get_rect(center=(self.border_thickness // 2, 
                                                row * self.square_size + self.square_size // 2 + self.border_thickness))  # Position on the left
            self.screen.blit(text, text_rect)

    def draw_pieces(self):
         # Draw pieces on the board
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece:  # If there is a piece
                    piece_image = piece.image  # Assuming each piece has an image attribute
                    self.screen.blit(piece_image, 
                                    (col * self.square_size + (self.square_size - piece_image.get_width()) // 2 + self.border_thickness,
                                    row * self.square_size + (self.square_size - piece_image.get_height()) // 2 + self.border_thickness))
        
    # Function to ascertain piece coordinates and move if fits logic
    # Each square of the 8X8 is either None or a Piece object
    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        piece = self.board[start_row][start_col]

        if piece and piece.is_move_valid(start_pos, end_pos, self.board):
            self.board[end_row][end_col] = piece # works for capturing too, sets the piece identity of the end position to the capturer
            self.board[start_row][start_col] = None # sets initial position of where the piece was to None
            return True

        return False

    
    def handle_click(self, row, col):
        if self.selected_piece: # checks if a piece is already selected
            # Try to move the selected piece to the clicked square
            if self.move_piece(self.selected_square, (row, col)): # function called with the start and end positions fed in
                # if move_piece returns True, it means the move was successful, deselect the pieces
                self.selected_piece = None
                self.selected_square = None
            else:
                # If move is invalid, deselect the pieces too
                self.selected_piece = None
                self.selected_square = None
        else:
            # Select a piece if one exists at the clicked square
            # If self.selected_piece is None, it means no piece is currently selected.
            piece = self.board[row][col]
            #checks the clicked square, self.board[row][col], to see if there is a piece there
            #If there is a piece (piece is not None), it sets self.selected_piece to this piece and self.selected_square to the square (row, col) where the piece is located.
            if piece:
                self.selected_piece = piece
                self.selected_square = (row, col)


