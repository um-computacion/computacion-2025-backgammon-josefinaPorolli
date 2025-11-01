"""Module for class board"""

from abc import ABC, abstractmethod
from typing import List, Any

class Field(ABC):
    """Basic interface for each type of field"""

    # Get the name of the field
    # Abstaract method indicates that the method will be
    # inherited by other classes and adapted to each class
    @abstractmethod
    def get_name(self) -> str:
        """Abstract method for get_name"""

    # Get the checkers in the field
    @abstractmethod
    def get_checkers(self) -> List[Any]:
        """Abstract method for get_checkers"""

class PointField(Field):
    """Represents normal points"""

    def __init__(self, point_number: int):
        self.__name__ = str(point_number)
        self.__checkers__ = []

    def get_name(self) -> str:
        return self.__name__

    def get_checkers(self) -> List[Any]:
        return self.__checkers__.copy()

class HouseField(Field):
    """Represents House fields"""

    def __init__(self, colour: str):
        self.__name__ = f"{colour}House"
        self.__checkers__ = []
        self.__color__ = colour

    def get_name(self) -> str:
        return self.__name__

    def get_checkers(self) -> List[Any]:
        return self.__checkers__.copy()

class EatenField(Field):
    """Represents eaten fields"""

    def __init__(self, colour: str):
        self.__name__ = f"{colour}Eaten"
        self.__checkers__ = []
        self.__color__ = colour

    def get_name(self) -> str:
        return self.__name__

    def get_checkers(self) -> List[Any]:
        return self.__checkers__.copy()

class Board:
    """Class representing the board of the game"""
    # CONSTRUCTOR - sets the attributes of the object
    def __init__(self):
        """Constructor: initializes the board with its points and other fields"""
        # The board is a dictionary. Its keys are the points,
        # houses or fields for "dead" checkers and its values are lists with the
        # checkers in the point or field.
        self.__board__ = self._initialize_board()

    def _initialize_board(self) -> dict:
        """Initialize the board using Field classes"""
        board = {}

        # The board has 24 points, initialized in 0. The checkers will be
        # added in the moment the game starts.
        for i in range(1, 25):
            point = PointField(i)
            board[str(i)] = point.get_checkers()

        # Places where the checkers have to be put in order to win
        board["BHouse"] = HouseField("B").get_checkers()
        board["WHouse"] = HouseField("W").get_checkers()

        # Places where the checkers are put in case they are eaten by another
        board["BEaten"] = EatenField("B").get_checkers()
        board["WEaten"] = EatenField("W").get_checkers()

        return board

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

    # SETTERS
    # This method receives a k parameter, which is field we want to add a checker to.
    # It also receives a checker parameter, representing the checker we want to add to the field.
    # It adds the checker to the field.
    # It does not return any value.
    def add_checker_to_field(self, k:str, checker):
        """Setter for adding a checker to a specific field"""
        self.__board__[k].append(checker)

    # This method receives a k parameter, which is the field we want to remove a checker from.
    # It removes the last checker added to the field.
    # It returns the checker that was removed from the field
    def remove_checker_from_field(self, k:str):
        """Setter for removing a checker from a specific field"""
        # pop() removes the checker from the field and returns it
        return self.__board__[k].pop()
