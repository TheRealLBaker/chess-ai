class TurnManager:
    def __init__(self):
        self.current_turn = 'W'  # White moves first

    def get_current_turn(self):
        """Returns the current turn ('W' for White, 'B' for Black)."""
        return self.current_turn

    def switch_turn(self):
        """Switches the turn between 'W' and 'B'."""
        self.current_turn = 'B' if self.current_turn == 'W' else 'W'

    def is_turn(self, colour):
        """Checks if it's the given colour's turn."""
        return self.current_turn == colour
