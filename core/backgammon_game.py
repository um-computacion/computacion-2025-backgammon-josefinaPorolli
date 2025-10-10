"""Module for class Backgammon Game"""
# This module is destinated to the class that manages the logic of the game.
from .board import Board
from .player import Player
from .dice import Dice
from .checker import Checker

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
        # Creating 15 checkers for each player
        self.__b_1__ = Checker(1, "Black")
        self.__b_2__ = Checker(2, "Black")
        self.__b_3__ = Checker(3, "Black")
        self.__b_4__ = Checker(4, "Black")
        self.__b_5__ = Checker(5, "Black")
        self.__b_6__ = Checker(6, "Black")
        self.__b_7__ = Checker(7, "Black")
        self.__b_8__ = Checker(8, "Black")
        self.__b_9__ = Checker(9, "Black")
        self.__b_10__ = Checker(10, "Black")
        self.__b_11__ = Checker(11, "Black")
        self.__b_12__ = Checker(12, "Black")
        self.__b_13__ = Checker(13, "Black")
        self.__b_14__ = Checker(14, "Black")
        self.__b_15__ = Checker(15, "Black")
        self.__w_1__ = Checker(16, "White")
        self.__w_2__ = Checker(17, "White")
        self.__w_3__ = Checker(18, "White")
        self.__w_4__ = Checker(19, "White")
        self.__w_5__ = Checker(20, "White")
        self.__w_6__ = Checker(21, "White")
        self.__w_7__ = Checker(22, "White")
        self.__w_8__ = Checker(23, "White")
        self.__w_9__ = Checker(24, "White")
        self.__w_10__ = Checker(25, "White")
        self.__w_11__ = Checker(26, "White")
        self.__w_12__ = Checker(27, "White")
        self.__w_13__ = Checker(28, "White")
        self.__w_14__ = Checker(29, "White")
        self.__w_15__ = Checker(30, "White")



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
    def get_destination_point(self, origin:str, steps:int) -> int:
        """This method returns the destination point given the origin and the steps."""
        if self.get_turn() == "Black":
            if origin == "BEaten":
                return str(steps)
            return str(int(origin) + steps)
        if self.get_turn() == "White":
            if origin == "WEaten":
                return str(25 - steps)
            return str(int(origin) - steps)
        raise ValueError(f"Could not get a valid turn: {self.get_turn()}")

    # METHODS FOR THE GAME

    # SET DEFAULT CHECKERS AT THE BEGINNING OF THE GAME
    # This method does not receive any parameters.
    # It sets the initial position of the checkers on the board.
    # It does not return any value.
    def set_default_checkers(self):
        """Method for setting the initial position of the checkers"""
        white_checkers = [self.__w_1__, self.__w_2__, self.__w_3__, self.__w_4__, self.__w_5__,
                          self.__w_6__, self.__w_7__, self.__w_8__, self.__w_9__, self.__w_10__,
                          self.__w_11__, self.__w_12__, self.__w_13__, self.__w_14__, self.__w_15__]
        black_checkers = [self.__b_1__, self.__b_2__, self.__b_3__, self.__b_4__, self.__b_5__,
                          self.__b_6__, self.__b_7__, self.__b_8__, self.__b_9__, self.__b_10__,
                          self.__b_11__, self.__b_12__, self.__b_13__, self.__b_14__, self.__b_15__]

        # Distribución para BLANCAS
        for _ in range(2):
            self.__board__.add_checker_to_field("24", white_checkers.pop())
        for _ in range(5):
            self.__board__.add_checker_to_field("13", white_checkers.pop())
        for _ in range(3):
            self.__board__.add_checker_to_field("8", white_checkers.pop())
        for _ in range(5):
            self.__board__.add_checker_to_field("6", white_checkers.pop())

        # Distribución para NEGRAS
        for _ in range(2):
            self.__board__.add_checker_to_field("1", black_checkers.pop())
        for _ in range(5):
            self.__board__.add_checker_to_field("12", black_checkers.pop())
        for _ in range(3):
            self.__board__.add_checker_to_field("17", black_checkers.pop())
        for _ in range(5):
            self.__board__.add_checker_to_field("19", black_checkers.pop())


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
            if len(self.__board__.get_checkers_in_field(destination)) > 0:
                if self.__board__.get_checkers_in_field(destination)[0].get_colour() == "White":
                    return True
            return False
        if self.get_turn() == "White":
            if len(self.__board__.get_checkers_in_field(destination)) > 0:
                if self.__board__.get_checkers_in_field(destination)[0].get_colour() == "Black":
                    return True
            return False
        raise ValueError(f"Could not get a valid turn: {self.get_turn()}")

    # This method receives the destination point as a parameter.
    # It checks if there is exactly one opponent checker in the destination point.
    # It returns True if there is exactly one opponent checker or False if there aren't.
    # If there is only one checker, it can be eaten.
    # This method is a part of the check_move method.
    def check_eatable_checker(self, destination:str) -> bool:
        """This method checks if there is exactly one opponent checker in the destination point"""
        if self.get_turn() == "Black":
            if len(self.__board__.get_checkers_in_field(str(destination))) == 1:
                if self.__board__.get_checkers_in_field(str(destination))[0].get_colour()=="White":
                    return True
            return False
        if self.get_turn() == "White":
            if len(self.__board__.get_checkers_in_field(str(destination))) == 1:
                if self.__board__.get_checkers_in_field(str(destination))[0].get_colour()=="Black":
                    return True
            return False
        raise ValueError(f"Could not get a valid turn: {self.get_turn()}")

    # This method receives destination as a parameter
    # It is a helper method for check_take_out_eaten_checker
    # It returns True if the checker can be taken out based
    # on the presence of an opponent checker. Otherwise, it returns False.
    def _check_take_out_with_opponent_checker(self, destination:str):
        """Helper method for check_take_out_eaten_checker"""
        if self.check_opponent_checkers(str(destination)):
            # Check if the checker is eatable
            if self.check_eatable_checker(str(destination)):
                return True
            return False
        return True

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
                return self._check_take_out_with_opponent_checker(str(steps))
            return False
        if self.get_turn() == "White":
            # Check if there are any eaten checkers
            if self.check_eaten_checkers("White"):
                # Check if the point where the checker has to enter
                # is not blocked by 2 or more black checkers
                return self._check_take_out_with_opponent_checker(str(25 - steps))
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
        """Helper method for check_move_to_house in Black case."""
        destination = self.get_destination_point(int(origin), steps)

        if int(destination) <= 24:
            return False  # Not a move to the black house

        # Check checkers out of the player's square or eaten checkers
        if self._black_checkers_out_of_square():
            return False

        # Check valid moves to take out checkers
        return self._is_valid_black_bear_off(steps)

    ############## SUB METHODS FOR CHECKING BLACK MOVE TO THE HOUSE ###################
    # This method does not receive any parameters.
    # It returns True if there are checkers out of the player's square and False if there aren't.
    def _black_checkers_out_of_square(self) -> bool:
        """Check if black has checkers outside home board or eaten."""
        # Check if there are checkers out of the player's square.
        for i in range(1, 19):
            for checker in self.__board__.get_checkers_in_field(str(i)):
                if checker.get_colour() == "Black":
                    return True

        # Check eaten checkers
        return self.check_eaten_checkers("Black")

    # This method receives steps as a parameter.
    # It returns True if the Black player can move checkers to the house and false if he/she can't.
    def _is_valid_black_bear_off(self, steps: int) -> bool:
        """Check if black can legally move to the house with the given steps."""
        point_to_check = 25 - steps

        # Check checkers in the exact point
        if self._black_checker_at_point(point_to_check):
            return True

        # Check further points
        for i_point in range(19, 25): # Checks all the points in the square
            if self._black_checker_at_point(i_point):
                # Returns True (valid move) if the checker is in the exact point or nearer
                return i_point >= point_to_check

        return False

    # This method receives an evaluated point.
    # Returns True if there are checkers in the exact point and False if there aren't.
    def _black_checker_at_point(self, point: int) -> bool:
        """Check if there's a black checker at given point."""
        for checker in self.__board__.get_checkers_in_field(str(point)):
            if checker.get_colour() == "Black":
                return True
        return False

    ######################################################################################

    # This method receives the origin point and the steps as parameters.
    # It is a sub method of check_move_to_house for white checkers.
    # It returns True if the checker can enter the house. It returns False if it can´t.
    def _check_white_move_to_house(self, origin: str, steps: int) -> bool:
        """Helper method for white's move to house."""
        destination = self.get_destination_point(int(origin), steps)

        if int(destination) >= 1:
            return False  # Not a move to house

        # Check if there are checkers out of the player's square or eaten checkers
        if self._white_checkers_out_of_square():
            return False

        # Check valid moves to take out checkers
        return self._is_valid_white_bear_off(steps)

    ############## SUB METHODS FOR CHECKING WHITE MOVE TO THE HOUSE ###################
    # This method does not receive any parameters.
    # It returns True if there are checkers out of the player's square and False if there aren't.
    def _white_checkers_out_of_square(self) -> bool:
        """Check if white has checkers outside home board or eaten."""
        # Check checkers out of the square
        for i in range(7, 25):
            for checker in self.__board__.get_checkers_in_field(str(i)):
                if checker.get_colour() == "White":
                    return True

        # Check eaten checkers
        return self.check_eaten_checkers("White")

    # This method receives steps as a parameter.
    # It returns True if the Black player can move checkers to the house and false if he/she can't.
    def _is_valid_white_bear_off(self, steps: int) -> bool:
        """Check if white can legally bear off with given steps."""
        point_to_check = steps

        # Check if there are checkers in the exact point
        if self._white_checker_at_point(point_to_check):
            return True

        # If there aren't checkers in the point, check further points in the same square.
        for i_point in range(6, 0, -1):
            if self._white_checker_at_point(i_point):
                # Returns True if the checker is in the exact point or nearer
                return i_point <= point_to_check

        return False

    # This method receives an evaluated point.
    # Returns True if there are checkers in the exact point and False if there aren't.
    def _white_checker_at_point(self, point: int) -> bool:
        """Check if there's a white checker at given point."""
        for checker in self.__board__.get_checkers_in_field(str(point)):
            if checker.get_colour() == "White":
                return True
        return False

    ######################################################################################

    # This method is a helper for check_move, checking specifically black moves.
    # It receives the current point and the steps as parameters
    # It returns True if the move is valid and false if it is not.
    def _check_black_move(self, point: str, steps: int) -> bool:
        # The moves will increment from 1 to 24
        destination = self.get_destination_point(point, steps)

        # First check if there are eaten checkers.
        # If there are, the player must take them out before moving any other checker.
        # First check if there are eaten checkers.
        if self.check_eaten_checkers("Black"):
            # If there are, check if it is possible to take one out with the given steps.
            return self.check_take_out_eaten_checker("Black")

        if int(destination) > 24: # If the checker tries to go off the board
            return self.check_move_to_house(point, steps) # Check if it can enter the house.

        # Check of there is any opponent checker in the destination point
        if self.check_opponent_checkers(destination):
            # If there are, we check if it is eatable (only 1 opponent checker)
            # If there is, the move is valid and the checker can be eaten.
            return self.check_eatable_checker(destination)
        return True

    # This method is a helper for check_move, checking specifically white moves.
    # It receives the current point and the steps as parameters
    # It returns True if the move is valid and false if it is not.
    def _check_white_move(self, point:str, steps:int) -> bool:
         # The moves will decrement from 24 to 1
        destination = self.get_destination_point(point, steps)

        # First check if there are eaten checkers.
        # If there are, the player must take them out before moving any other checker.
        # First check if there are eaten checkers.
        if self.check_eaten_checkers("White"):
            # If there are, check if it is possible to take one out with the given steps.
            return self.check_take_out_eaten_checker("White")

        if int(destination) < 1: # If the checker tries to go off the board
            return self.check_move_to_house(point, steps) # Check if it can enter the house.

        # Check of there is any opponent checker in the destination point
        if self.check_opponent_checkers(destination):
            # If there are, we check if it is eatable (only 1 opponent checker)
            return self.check_eatable_checker(destination)
        return True

    # This method receives the point where the chosen checker is and the steps as parameters.
    # It returns True if the move is valid or not.
    # Returns False if the move is not valid. Returns True if the move is valid.
    def check_move(self, point:str, steps:int) -> bool:
        """This method evaluates if the move that is going to be made is valid"""
        if self.get_turn() == "Black":
            return self._check_black_move(point, steps)
        if self.get_turn() == "White":
            return self._check_white_move(point, steps)
        return False # Default

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
