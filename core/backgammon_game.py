"""Module for class Backgammon Game"""
# This module is destinated to the class that manages the logic of the game.
from board import Board
from player import Player
from dice import Dice
from checker import Checker

# --- Methods to be added (temporary comment)---
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
    
    # This method receives the origin point and the steps as parameters.
    # It returns the destination point given the origin and the steps.
    def get_destination_point(self, origin:int, steps:int) -> int:
        """This method returns the destination point given the origin and the steps."""
        if self.get_turn() == "Black":
            if origin == "BEaten":
                return steps
            return origin + steps
        elif self.get_turn() == "White":
            if origin == "WEaten":
                return 25 - steps
            return origin - steps

    # METHODS FOR THE GAME
    
    # -------------- CHECK MOVES --------------

    # This method receives the colour of the player as a parameter.
    # It checks if the player has eaten checkers that must enter the board before moving other checkers.
    # It returns True if there are eaten checkers or False if there aren't.
    # This method is a part of the check_move method.
    def check_eaten_checkers(self, colour:str) -> bool:
        """This method checks if the player has checkers in the 'eaten' field"""
        if colour == "Black":
            if len(self.__board__.get_checkers_in_field("BEaten")) > 0:
                # If there are any checkers in the "eaten" field, there are eaten checkers.
                return True
            # If there are no checkers in the mentioned field, there are no eaten checkers.
            return False
        elif colour == "White":
            if len(self.__board__.get_checkers_in_field("WEaten")) > 0:
                # If there are any checkers in the "eaten" field, there are eaten checkers.
                return True
            # If there are no checkers in the mentioned field, there are no eaten checkers.
            return False

    # This method receives the destination point as a parameter.
    # It checks if there are more than 1 opponent checkers in the destination point.
    # It returns True if there are opponent checkers or False if there aren't.
    # This method is a part of the check_move method.
    def check_opponent_checkers(self, destination:int) -> bool:
        """This method checks if there are more than 1 opponent checkers in the destination point"""
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
    
    # This method receives the destination point as a parameter.
    # It checks if there is exactly one opponent checker in the destination point.
    # It returns True if there is exactly one opponent checker or False if there aren't.
    # If there is only one checker, it can be eaten.
    # This method is a part of the check_move method.
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
    
    # This method receives steps as parameters.
    # It evaluates if a checker can be taken out of the eaten field
    # It returns true if the move is valid. It returns false if the move is not valid.
    # This method is a part of the check_move method.
    def check_take_out_eaten_checker(self, steps:int) -> bool:
        """This method checks if the player can take out an eaten checker"""
        if self.get_turn() == "Black":
            # Check if there are any eaten checkers
            if self.check_eaten_checkers("Black"):
                # Check if the point where the checker has to enter is not blocked by 2 or more white checkers
                if self.check_opponent_checkers(steps):
                    return False
                return True
            return False
        elif self.get_turn() == "White":
            # Check if there are any eaten checkers
            if self.check_eaten_checkers("White"):
                # Check if the point where the checker has to enter is not blocked by 2 or more black checkers
                if self.check_opponent_checkers(25 - steps):
                    return False
                return True
            return False
    


    # This method receives the point where the chosen checker is and the steps it has to move as parameters.
    # It returns True if the move is valid or not. Just checks basic moves, like not going off the board.
    # Returns False if the move is not valid. Returns True if the move is valid.
    def check_move(self, point:str, steps:int) -> bool:
        """This method evaluates if the move that is going to be made is valid"""
        if self.get_turn() == "Black":

            # The moves will increment from 1 to 24
            destination = self.get_destination_point(point, steps)

            # First check if there are eaten checkers. If there are, the player must take them out before moving any other checker.
            # First check if there are eaten checkers.
            if self.check_eaten_checkers("Black"):
                # If there are, check if it is possible to take one out with the given steps.
                if self.check_take_out_eaten_checker("Black"):
                    return True
                return False

            elif destination > 24: # If the checker tries to go off the board

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
            elif self.check_opponent_checkers(destination):
                # If there are, we check if it is eatable (only 1 opponent checker)
                if self.check_eatable_checker(destination):
                    # If there is, the move is valid and the checker can be eaten.
                    return True
                return False
            return True
            
        elif self.get_turn() == "White":

            # The moves will decrement from 24 to 1
            destination = self.get_destination_point(point, steps)

            # First check if there are eaten checkers. If there are, the player must take them out before moving any other checker.
            # First check if there are eaten checkers.
            if self.check_eaten_checkers("Black"):
                # If there are, check if it is possible to take one out with the given steps.
                if self.check_take_out_eaten_checker("Black"):
                    return True
                return False

            elif destination < 1:
                # Check if all the checkers are in the player's square.
                # If they are not, the move is not valid. If they are, we proceed with the next conditionals.
                # a. Check that there are no white checkers in points 1 to 18
                for i in range(7, 25):
                    for checker in self.__board__.get_checkers_in_field(str(i)):
                        if checker.get_colour() == "White":
                            # If there is any white checker out of the square, the move is not valid.
                            return False
                        else:
                            # b. Check that there are no white eaten checkers
                            if self.check_eaten_checkers("White"):
                                # If there are, the move is not valid.
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
            elif self.check_opponent_checkers(destination):
                # If there are, we check if it is eatable (only 1 opponent checker)
                if self.check_eatable_checker(destination):
                    return True
                return False
            return True
        
    # -------------- MAKE MOVES --------------

    # This method receives the origin point and the destination point as parameters.
    # It moves the checker from origin to destination.
    # It does not return any value.
    def move_checker(self, origin:str, destination:str):
        """This method moves the checker from origin to destination"""
        moving_checker = self.__board__.remove_checker_from_field(origin)
        self.__board__.add_checker_to_field(destination, moving_checker)
    
    # This method receives the origin point as a parameter.
    # It moves the opponent checker to the "eaten" field.
    # It does not return any value.
    def eat_opponent_checker(self, origin:int):
        """This method moves the opponent checker to the 'eaten' field"""
        if self.get_turn() == "Black":
            eaten_checker = self.__board__.remove_checker_from_field(str(origin))
            self.__board__.add_checker_to_field("WEaten", eaten_checker)
        elif self.get_turn() == "White":
            eaten_checker = self.__board__.remove_checker_from_field(str(origin))
            self.__board__.add_checker_to_field("BEaten", eaten_checker)

    # This method receives the steps as a parameter.
    # It takes the checker from the "eaten" field and puts it back on the board.
    # It does not return any value.
    def take_out_eaten_checker(self, steps:int):
        """This method takes the checker out of the 'eaten' field and puts it back on the board."""
        if self.get_turn() == "Black":
            checker_to_put_back = self.__board__.remove_checker_from_field("BEaten")
            self.__board__.add_checker_to_field(str(steps), checker_to_put_back)
        elif self.get_turn() == "White":
            checker_to_put_back = self.__board__.remove_checker_from_field("WEaten")
            self.__board__.add_checker_to_field(str(25 - steps), checker_to_put_back)

    # This method receives the origin point as a parameter.
    # It moves a checker from the origin to the player's house.
    # It does not return any values.
    def move_checker_to_house(self, origin:int):
        # Under the condition that the checker can be moved to the house, the origin is supposed to be an int.
        if self.get_turn() == "Black":
            self.move_checker(origin, "BHouse")
        elif self.get_turn() == "White":
            self.move_checker(origin, "WHouse")
        
