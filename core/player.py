"""Module for class Player"""

from abc import ABC, abstractmethod

class IPlayer(ABC):
    """Player abstracion"""

    @abstractmethod
    def set_name(self, name: str) -> None:
        """Abstract method for set_name"""

    @abstractmethod
    def set_colour(self, colour: str) -> None:
        """Abstract method for set_colour"""

    @abstractmethod
    def get_name(self) -> str:
        """Abstract method for get_name"""

    @abstractmethod
    def get_colour(self) -> str:
        """Abstract method for get_colour"""

class Player:
    """Class representing a player in the game"""
    # CONSTRUCTOR
    # The constructor in every class sets the initial state of the object and its attributes
    def __init__(self, name:str, colour:str):
        """Constructor of the class Player"""
        self.__name__ = name # Each player will introduce themselves with their names before playing
        self.__colour__ = colour # The game will assign a colour to each player

    # SETTERS

    # This function receives the player's name before starting the game.
    # The purpose of this function is to set the player's name.
    # The function does not return any values, since it is a setter
    def set_name(self, name:str):
        """Method for setting the player's name"""
        self.__name__ = name

    # At the beginning of the game, the colours of each player are set.
    # The purpose of this function is to set the player's colour.
    # The function does not return any values, since it is a setter
    def set_colour(self, colour:str):
        """Method for setting the player's colour"""
        self.__colour__ = colour

    # GETTERS

    # This function does not receive any parameters, for it is just a getter.
    # The purpose of this function is to get the player's name
    # This function returns a string, which corresponds to the player's name
    def get_name(self) -> str:
        """Method for getting the player's name"""
        return self.__name__

    # This function does not receive any parameters, for it is just a getter.
    # The purpose of this function is to get the player's colour
    # This function returns a string, which corresponds to the player's colour
    def get_colour(self) -> str:
        """Method for getting the player's colour"""
        return self.__colour__
