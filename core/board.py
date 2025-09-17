"""Module for class board"""

class Board:
    """Class representing the board of the game"""
    # CONSTRUCTOR - sets the attributes of the object
    def __init__(self):
        """Constructor: initializes the board with its points and other fields"""
        # The board is a dictionary. Its keys are the points,
        # houses or fields for "dead" checkers and its values are lists with the
        # checkers in the point or field.
        self.__board__ = {
            # The board has 24 points, initialized in 0. The ckeckers will be
            # added in the moment the game starts.
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [],
            "9": [],
            "10": [],
            "11": [],
            "12": [],
            "13": [],
            "14": [],
            "15": [],
            "16": [],
            "17": [],
            "18": [],
            "19": [],
            "20": [],
            "21": [],
            "22": [],
            "23": [],
            "24": [],
            # Places where the checkers have to be put in order to win
            "BHouse": [],
            "Whouse": [],
            # Places where the checkers are put in case they are eaten by another
            "BEaten": [],
            "WEaten": []
        }


    # GETTERS
    # This method does not receive any parameters.
    # It returns the current state of the board.
    def get_board(self) -> dict:
        """Getter for the board"""
        return self.__board__

    # This method receives a k parameter, representing the index of the field we want to evaluate
    # It returns the current state of the point or field in the board
    def get_checkers_in_field(self, k:str) -> list:
        """Getter for the checkers in a specific field"""
        return self.__board__[k]
