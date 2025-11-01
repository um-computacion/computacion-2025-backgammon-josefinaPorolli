"""Module for class checker"""

class Checker:
    """Class for each checker of the game"""
    # CONSTRUCTOR - sets the attributes of the object
    def __init__(self, checker_id: int, colour: str):
        """Constructor: initializes the checker with an id and a colour"""
        self.__id__ = checker_id # Unique identifier for the checker
        self.__colour__ = colour # Colour of the checker

    # Getters
    # This method does not receive any parameters.
    # It returns the current value of the checker id.
    def get_id(self) -> str:
        """Getter for the checker id"""
        return self.__id__

    # This method does not receive any parameters.
    # It returns the current value of the checker colour.
    def get_colour(self) -> str:
        """Getter for the checker colour"""
        return self.__colour__
