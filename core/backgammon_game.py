"""Module for class Backgammon Game"""
# This module is destinated to the class that manages the logic of the game.
from board import Board
from player import Player
from dice import Dice
from checker import Checker

# --- Methods to be added (temporary comment)---
# Move checker
# Check if a checker's been eaten
# Check if all the checkers of the player are in the player's square
# Check if the checker can be moved to the house
# Check winner

class BackgammonGame:
    """Class with the methods for the logic of the game"""
    # CONSTRUCTOR - sets the main attributes of the class
    def __init__(self):
        self.__turn__ = None
        self.__board__ = Board()
        self.__dice1__ = Dice()
        self.__dice2__ = Dice()
        self.__player1__ = Player("Player 1", "White")
        self.__player2__ = Player("Player 2", "Black")
    
    # ---------- TURNS -------------
    # SETTER
    def set_turn(self, colour):
        """Sets the colour of the player whose turn is"""
        self.__turn__ = colour
    
    # GETTER
    def get_turn(self) -> str:
        """Returns the colour of the player whose turn is"""
        return self.__turn__
    
    # METHODS FOR THE GAME

    # ------------- BASIC MOVES -------------
    # This method will be fixed by implementing the logic of eaten checkers and moves to the house.
    # I also need to check if there are checkers corresponding to the rival in the destination
    def check_move(self, point:int, steps:int) -> bool:
        """This method evaluates if the move that is going to be made is valid"""
        if self.get_turn() == "Black":
            # The moves will increment from 1 to 24
            destination = point + steps
            if destination > 24:
                return False
            return True
            
        elif self.get_turn() == "White":
            # The moves will decrement from 1 to 24
            destination = point - steps
            if destination < 1:
                return False
            return True
