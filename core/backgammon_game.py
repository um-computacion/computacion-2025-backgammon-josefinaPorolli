"""Module for class Backgammon Game"""
# This module is destinated to the class that manages the logic of the game.
from .board import Board
from .player import Player
from .dice import Dice

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
    # SETTERS
    # This method receives the colour of the player as a parameter.
    # It sets 'turn' with the colour of the player whose turn is.
    def set_turn(self, colour):
        """Sets the colour of the player whose turn is"""
        self.__turn__ = colour

    # This method does not receive any parameters.
    # It checks if the 15 checkers of a player is in the house
    # If there are 15 checkers in one of the houses, it sets the winner.
    # It returns "None" (as string for preventing problems)
    # if there is no winner or the colour of the winner if there is.
    def check_winner(self) -> str:
        """This method checks if there is a winner."""
        if len(self.__board__.get_checkers_in_field("BHouse")) == 15:
            return "Black"
        if len(self.__board__.get_checkers_in_field("WHouse")) == 15:
            return "White"
        return "None"

    # GETTERS
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
        if self.get_turn() == "White":
            if origin == "WEaten":
                return 25 - steps
            return origin - steps
        raise ValueError(f"Could not get a valid turn: {self.get_turn()}")

    # METHODS FOR THE GAME

    # -------------- CHECK MOVES --------------

    # This method receives the colour of the player as a parameter.
    # It checks if the player has eaten checkers that must enter
    # the board before moving other checkers.
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
        if colour == "White":
            if len(self.__board__.get_checkers_in_field("WEaten")) > 0:
                # If there are any checkers in the "eaten" field, there are eaten checkers.
                return True
            # If there are no checkers in the mentioned field, there are no eaten checkers.
            return False
        raise ValueError(f"Could not get a valid colour: {colour}")

    # This method receives the destination point as a parameter.
    # It checks if there are more than 1 opponent checkers in the destination point.
    # It returns True if there are opponent checkers or False if there aren't.
    # This method is a part of the check_move method.
    def check_opponent_checkers(self, destination:str) -> bool:
        """This method checks if there are more than 1 opponent checkers in the destination point"""
        if self.get_turn() == "Black":
            if len(self.__board__.get_checkers_in_field(int(destination))) > 0:
                if self.__board__.get_checkers_in_field((destination))[0].get_colour() == "White":
                    return True
            return False
        if self.get_turn() == "White":
            if len(self.__board__.get_checkers_in_field(int(destination))) > 0:
                if self.__board__.get_checkers_in_field((destination))[0].get_colour() == "Black":
                    return True
            return False
        raise ValueError(f"Could not get a valid turn: {self.get_turn()}")

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
        if self.get_turn() == "White":
            if len(self.__board__.get_checkers_in_field(str(destination))) == 1:
                if self.__board__.get_checkers_in_field(str(destination))[0] == "Black":
                    return True
            return False
        raise ValueError(f"Could not get a valid turn: {self.get_turn()}")

    # This method receives steps as parameters.
    # It evaluates if a checker can be taken out of the eaten field
    # It returns true if the move is valid. It returns false if the move is not valid.
    # This method is a part of the check_move method.
    def check_take_out_eaten_checker(self, steps:int) -> bool:
        """This method checks if the player can take out an eaten checker"""
        if self.get_turn() == "Black":
            # Check if there are any eaten checkers
            if self.check_eaten_checkers("Black"):
                # Check if the point where the checker has to enter
                # is not blocked by 2 or more white checkers
                if self.check_opponent_checkers(steps):
                    return False
                return True
            return False
        if self.get_turn() == "White":
            # Check if there are any eaten checkers
            if self.check_eaten_checkers("White"):
                # Check if the point where the checker has to enter
                # is not blocked by 2 or more black checkers
                if self.check_opponent_checkers(25 - steps):
                    return False
                return True
            return False
        raise ValueError(f"Could not get a valid turn: {self.get_turn()}")

    # This method receives the origin and the steps as parameters.
    # It checks if a checker can be moved to the house.
    # It returns True if the move is valid. It returns False if:
    # 1. Not all checkers are in the player's square
    # 2. The steps don't match the origin point with the steps to the house
    # AND there are checkers further than the number the steps allow.
    def check_move_to_house(self, origin: str, steps: int) -> bool:
        """Checks if a checker can be moved to the house."""
        turn = self.get_turn()

        if turn == "Black":
            return self._check_black_move_to_house(origin, steps)
        if turn == "White":
            return self._check_white_move_to_house(origin, steps)
        raise ValueError(f"Could not get a valid turn: {turn}")

    # This method receives the origin point and the steps as parameters.
    # It is a sub method of check_move_to_house for black checkers.
    # It returns True if the checker can enter the house. It returns False if it can´t.
    def _check_black_move_to_house(self, origin: str, steps: int) -> bool:
        """Helper method for black's move to house."""
        destination = self.get_destination_point(int(origin), steps)

        if destination <= 24:
            return False  # Not a move to black house

        # Check if there are checkers out of the square
        for i in range(1, 19):
            for checker in self.__board__.get_checkers_in_field(str(i)):
                if checker.get_colour() == "Black":
                    return False

        # Check if there are eaten checkers
        if self.check_eaten_checkers("Black"):
            return False

        # Check valid movements to take out checkers
        point_to_check = 25 - steps # Checks the point
        checkers_at_point = self.__board__.get_checkers_in_field(str(point_to_check))

        # If there are checkers in the point, the move is valid.
        for checker in checkers_at_point:
            if checker.get_colour() == "Black":
                return True

        # If there are not, we check further points
        for i_point in range(19, point_to_check + 1):
            checkers_at_i = self.__board__.get_checkers_in_field(str(i_point))
            for checker in checkers_at_i:
                if checker.get_colour() == "Black":
                    # If there are checkers in further points, the move is not valid.
                    if i_point < point_to_check:
                        return False
                    return True

        return False  # Default case

    # This method receives the origin point and the steps as parameters.
    # It is a sub method of check_move_to_house for white checkers.
    # It returns True if the checker can enter the house. It returns False if it can´t.
    def _check_white_move_to_house(self, origin: str, steps: int) -> bool:
        """Helper method for white's move to house."""
        destination = self.get_destination_point(int(origin), steps)

        if destination >= 1:
            return False  # Not a move to the white house

        # Check if there are no checkers out of the player's square
        for i in range(7, 25):
            for checker in self.__board__.get_checkers_in_field(str(i)):
                if checker.get_colour() == "White":
                    return False

        # Check if there are eaten checkers.
        if self.check_eaten_checkers("White"):
            return False

        # Check valid movements to take out checkers
        point_to_check = steps
        checkers_at_point = self.__board__.get_checkers_in_field(str(point_to_check))

        # If there are checkers in the exact point, the move is valid.
        for checker in checkers_at_point:
            if checker.get_colour() == "White":
                return True

        # Check further points in case there are no checkers in the exact point.
        for i_point in range(6, point_to_check - 1, -1):
            checkers_at_i = self.__board__.get_checkers_in_field(str(i_point))
            for checker in checkers_at_i:
                if checker.get_colour() == "White":
                    # If there are checkers in further points, it is not valid.
                    if i_point > point_to_check:
                        return False
                    return True

        return False  # Default case.

    # This method receives the point where the chosen checker is and the steps as parameters.
    # It returns True if the move is valid or not.
    # Returns False if the move is not valid. Returns True if the move is valid.
    def check_move(self, point:str, steps:int) -> bool:
        """This method evaluates if the move that is going to be made is valid"""
        if self.get_turn() == "Black":

            # The moves will increment from 1 to 24
            destination = self.get_destination_point(point, steps)

            # First check if there are eaten checkers.
            # If there are, the player must take them out before moving any other checker.
            # First check if there are eaten checkers.
            if self.check_eaten_checkers("Black"):
                # If there are, check if it is possible to take one out with the given steps.
                if self.check_take_out_eaten_checker("Black"):
                    return True
                return False

            if destination > 24: # If the checker tries to go off the board
                if self.check_move_to_house(point, steps): # Check if it can enter the house.
                    return True
                return False

            # Check of there is any opponent checker in the destination point
            if self.check_opponent_checkers(destination):
                # If there are, we check if it is eatable (only 1 opponent checker)
                if self.check_eatable_checker(destination):
                    # If there is, the move is valid and the checker can be eaten.
                    return True
                return False
            return True

        if self.get_turn() == "White":

            # The moves will decrement from 24 to 1
            destination = self.get_destination_point(point, steps)

            # First check if there are eaten checkers.
            # If there are, the player must take them out before moving any other checker.
            # First check if there are eaten checkers.
            if self.check_eaten_checkers("Black"):
                # If there are, check if it is possible to take one out with the given steps.
                if self.check_take_out_eaten_checker("Black"):
                    return True
                return False

            if destination < 1: # If the checker tries to go off the board
                if self.check_move_to_house(point, steps): # Check if it can enter the house.
                    return True
                return False

            # Check of there is any opponent checker in the destination point
            if self.check_opponent_checkers(destination):
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
        """Moves a checker to the player's house"""
        # Removed check for entering the house. Needed steps as parameter (useless in this method).
        # The actual check will be done during the game
        if self.get_turn() == "Black":
            self.move_checker(origin, "BHouse")
        elif self.get_turn() == "White":
            self.move_checker(origin, "WHouse")
