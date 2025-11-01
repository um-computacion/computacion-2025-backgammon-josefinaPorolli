"""Module for dice class."""

import random
from abc import ABC, abstractmethod


# FOR DIP
class IDice(ABC):
    """Abstraction for Dice"""
    @abstractmethod
    def roll(self) -> int:
        pass
    
    @abstractmethod
    def get_number(self) -> int:
        pass

class Dice(IDice):
    """Class representing a dice."""
    # CONSTRUCTOR - sets the attributes of the object.
    def __init__(self):
        """Initializes the dice with its current value and possible ones"""
        self.__values__ = [1, 2, 3, 4, 5, 6] # The dice is 6-sided
        # The current value of the dice initially is none as it has not been rolled yet
        self.__current_value__ = None

    # GETTER
    # This method does not receive any parameters.
    # It returns the current value of the dice.
    def get_number(self):
        """Returns the current value of the dice."""
        return self.__current_value__

    # METHOD - ROLLER
    # This method does not receive any parameters.
    # It simulates rolling a dice.
    # It returns the value of the dice.
    def roll(self):
        """Simulates rolling the dice and returns its value."""
        self.__current_value__ = random.randint(1,6)
        return self.get_number()
