"""Module for class checker"""

class Checker:
    """Class for each checker of the game"""
    # CONSTRUCTOR - sets the attributes of the object
    def __init__(self, colour: str):
        """Constructor: initializes the checker with an id and a colour"""
        self.__id__ = id(self) # Unique identifier for each checker depending on its memory address
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

    # Setter
    # This method receives a parameter colour to assign a colour to every checker.
    # It does not return any value.
    def set_colour(self, colour: str) -> None:
        """Setter for the checker colour"""
        self.__colour__ = colour
