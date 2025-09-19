"""Module for class Backgammon Game"""
# This module is destinated to the class that manages the logic of the game.
from board import Board
from player import Player
from dice import Dice
from checker import Checker

# --- Methods to be added (temporary comment)---
# Move checker
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
    # This method receives the colour of the player as a parameter.
    # It sets 'turn' with the colour of the player whose turn is.
    def set_turn(self, colour):
        """Sets the colour of the player whose turn is"""
        self.__turn__ = colour
    
    # GETTER
    # This method does not receive any parameters.
    # It returns the colour of the player whose turn is.
    def get_turn(self) -> str:
        """Returns the colour of the player whose turn is"""
        return self.__turn__
    
    # METHODS FOR THE GAME
    
    # -------------- CHECK MOVES --------------

    # Check if the player has eaten checkers that must enter the board before moving other checkers.
    def check_eaten_checkers(self, colour:str) -> bool:
        """This method checks if the player has checkers in the 'eaten' field"""
        if colour == "Black":
            if len(self.__board__.get_checkers_in_field("BEaten")) > 0:
                return True
            return False
        elif colour == "White":
            if len(self.__board__.get_checkers_in_field("WEaten")) > 0:
                return True
            return False

    def check_opponent_checkers(self, destination:int) -> bool:
        """This method checks if there are more than 1 opponent checkers in the destination point"""
        # If there is one opponent checker, it can be eaten.
        if self.get_turn() == "Black":
            if len(self.__board__.get_checkers_in_field(str(destination))) > 0:
                if self.__board__.get_checkers_in_field(str(destination))[0].get_colour() == "White":
                    return True
            return False
        elif self.get_turn() == "White":
            if len(self.__board__.get_checkers_in_field(str(destination))) > 0:
                if self.__board__.get_checkers_in_field(str(destination))[0].get_colour() == "Black":
                    return True
            return False
    
    def check_eatable_checker(self, destination:int) -> bool:
        """This method checks if there is exactly one opponent checker in the destination point"""
        if self.get_turn() == "Black":
            if len(self.__board__.get_checkers_in_field(str(destination))) == 1:
                if self.__board__.get_checkers_in_field(str(destination))[0] == "White":
                    return True
            return False
        elif self.get_turn() == "White":
            if len(self.__board__.get_checkers_in_field(str(destination))) == 1:
                if self.__board__.get_checkers_in_field(str(destination))[0] == "Black":
                    return True
            return False

    # This method receives the point where the chosen checker is and the steps it has to move as parameters.
    # It returns True if the move is valid or not. Just checks basic moves, like not going off the board.
    # Returns False if the move is not valid. Returns True if the move is valid.
    def check_move(self, point:int, steps:int) -> bool:
        """This method evaluates if the move that is going to be made is valid"""
        if self.get_turn() == "Black":
            # The moves will increment from 1 to 24
            destination = point + steps
            if destination > 24: # If the checker tries to go off the board

                # Check if all the checkers are in the player's square.
                # If they are not, the move is not valid. If they are, we proceed with the next conditionals.
                # a. Check that there are no black checkers in points 1 to 18
                for i in range(1, 19):
                    for checker in self.__board__.get_checkers_in_field(str(i)):
                        if checker.get_colour() == "Black":
                            return False
                        else:
                            # b. Check that there are no black eaten checkers
                            if self.check_eaten_checkers("Black"):
                                return False
                            else:
                                # Check if there is a checker in the point that is exactly 25 - steps.
                                for checker in self.__board__.get_checkers_in_field(str(25 - steps)):
                                    if checker.get_colour() == "Black":
                                        return True
                                    else:
                                        # Check if there are checkers in points further than 25 - steps. If there are, the move is not valid.
                                        for i_point in range(19, 25 - steps + 1): # from 19 (furthest in the square) to selected point (inclusive)
                                            for checker in self.__board__.get_checkers_in_field(str(i_point)):
                                                if checker.get_colour() == "Black":
                                                    if i_point < (25 - steps): # Check if i_point is further than 25 - steps
                                                        return False
                                                    else:
                                                        return True
                                                else:
                                                    return True
            
            # Check of there is any opponent checker in the destination point
            if self.check_opponent_checkers(destination):
                # If there are, we check if it is eatable (only 1 opponent checker)
                if self.check_eatable_checker(destination):
                    return True
                return False
            return True
            
        elif self.get_turn() == "White":
            # The moves will decrement from 24 to 1
            destination = point - steps
            if destination < 1:
                # Check if all the checkers are in the player's square.
                # If they are not, the move is not valid. If they are, we proceed with the next conditionals.
                # a. Check that there are no white checkers in points 1 to 18
                for i in range(7, 25):
                    for checker in self.__board__.get_checkers_in_field(str(i)):
                        if checker.get_colour() == "White":
                            return False
                        else:
                            # b. Check that there are no white eaten checkers
                            if self.check_eaten_checkers("White"):
                                return False
                            else:
                                # Check if there is a checker in the point that is exactly 0 + steps.
                                for checker in self.__board__.get_checkers_in_field(str(steps)):
                                    if checker.get_colour() == "White":
                                        return True
                                    else:
                                        # Check if there are checkers in points further than 0 + steps. If there are, the move is not valid.
                                        for i_point in range(6, steps - 1, -1): # from 6 (furthest in the square) to selected point (inclusive)
                                            for checker in self.__board__.get_checkers_in_field(str(i_point)):
                                                if checker.get_colour() == "White":
                                                    if i_point < (steps): # Check if i_point is further than 0 + steps
                                                        return False
                                                    else:
                                                        return True
                                                else:
                                                    return True
            
            # Check of there is any opponent checker in the destination point
            if self.check_opponent_checkers(destination):
                # If there are, we check if it is eatable (only 1 opponent checker)
                if self.check_eatable_checker(destination):
                    return True
                return False
            return True
        
    # -------------- MAKE MOVES --------------
    
    def eat_opponent_checker(self, origin:int):
        """This method moves the opponent checker to the 'eaten' field"""
        if self.get_turn() == "Black":
            # pop() removes the checker and returns it
            eaten_checker = self.__board__.get_checkers_in_field(str(origin)).pop()
            self.__board__.get_checkers_in_field("WEaten").append(eaten_checker)
        elif self.get_turn() == "White":
            eaten_checker = self.__board__.get_checkers_in_field(str(origin)).pop()
            self.__board__.get_checkers_in_field("BEaten").append(eaten_checker)
        
