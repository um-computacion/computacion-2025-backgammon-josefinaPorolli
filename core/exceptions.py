"""Module for exceptions in core/"""

class InvalidTurnError(Exception):
    """Invalid turn exception"""
    def __init__(self, turn, message="Could not get a valid turn"):
        self.turn = turn
        self.message = f"{message}: {turn}"
        super().__init__(self.message)

class InvalidColourError(Exception):
    """Invalid colour exception"""
    def __init__(self, colour, message="Could not get a valid colour"):
        self.colour = colour
        self.message = f"{message}: {colour}"
        super().__init__(self.message)
