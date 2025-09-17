"""Module for class board"""

class Board:
    """Class representing the board of the game"""
    # CONSTRUCTOR - sets the attributes of the object
    def __init__(self):
        """Constructor: initializes the board with its points and other fields"""
        # The board is a dictionary. Its keys are the points,
        # houses or fields for "dead" checkers and its values are lists with the
        # quantity of checkers in the ponit and the colour of the checkers.
        self.__board__ = {
            # The board has 24 points, initialized with the corresponding quantity of checkers.
            "1": [2, "B"],
            "2": [0, "-"],
            "3": [0, "-"],
            "4": [0, "-"],
            "5": [0, "-"],
            "6": [5, "W"],
            "7": [0, "-"],
            "8": [3, "W"],
            "9": [0, "-"],
            "10": [0, "-"],
            "11": [0, "-"],
            "12": [5, "B"],
            "13": [5, "W"],
            "14": [0, "-"],
            "15": [0, "-"],
            "16": [0, "-"],
            "17": [3, "B"],
            "18": [0, "-"],
            "19": [5, "B"],
            "20": [0, "-"],
            "21": [0, "-"],
            "22": [0, "-"],
            "23": [0, "-"],
            "24": [2, "W"],
            # Places where the checkers have to be put in order to win
            "BHouse": [0, "-"],
            "Whouse": [0, "-"],
            # Places where the checkers are put in case they are eaten by another
            "BEaten": [0, "-"],
            "WEaten": [0, "-"]
        }


    # GETTERS
    # This method does not receive any parameters.
    # It returns the current state of the board.
    def get_board(self) -> dict:
        """Getter for the board"""
        return self.__board__

    # This method receives a k parameter, representing the index of the field we want to evaluate
    # It returns the current state of the point or field in the board
    def get_checkers_in_point(self, k:str) -> list:
        """Getter for the quantity of checkers and their colours in a specific field"""
        return self.__board__[k]
