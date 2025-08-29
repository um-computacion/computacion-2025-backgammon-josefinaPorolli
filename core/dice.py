import random

class Dice:
    # CONSTRUCTOR - sets the attributes of the object.
    def __init__(self):
        self.__values__ = [1, 2, 3, 4, 5, 6] # The dice is 6-sided
        self.__current_value__ = None # The current value of the dice initially is none as it has not been rolled yet
    
    # GETTER
    # This method does not receive any parameters.
    # It returns the current value of the dice.
    def get_number(self):
        return self.__current_value__
    
    # METHOD - ROLLER
    # This method does not receive any parameters.
    # It simulates rolling a dice.
    # It returns the value of the dice.
    def roll(self):
        self.__current_value__ = random.choice(self.__values__)
        return self.get_number()


