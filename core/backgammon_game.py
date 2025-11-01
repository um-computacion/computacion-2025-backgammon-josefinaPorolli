"""Module for class Backgammon Game"""
# This module is destinated to the class that manages the logic of the game.
from typing import List, Optional, Callable
from abc import ABC, abstractmethod
from .board import Board
from .player import Player, IPlayer
from .dice import Dice, IDice
from .checker import Checker
from .exceptions import InvalidColourError, InvalidTurnError

# Abstraction for CheckMoves
class IMoveValidator(ABC):
    """Abstract class for check_move"""
    @abstractmethod
    def check_move(self, point: str, steps: int) -> bool:
        """Abstract method for check_move"""

    @abstractmethod
    def check_take_out_eaten_checker(self, steps: int) -> bool:
        """Abstract method for check_take_out_eaten_checker"""

    @abstractmethod
    def check_opponent_checkers(self, destination: str) -> bool:
        """Abstract method for check_opponent_checkers"""

    @abstractmethod
    def check_eatable_checker(self, destination: str) -> bool:
        """Abstract method for check_eatable_checker"""

    @abstractmethod
    def check_move_to_house(self, origin: str, steps: int) -> bool:
        """Abstract method for check_move_to_house"""

# Abstraction for CheckerFactory
class ICheckerFactory(ABC):
    """Abstract class for checker factory"""
    @abstractmethod
    def create_checker_set(self, colour: str, start_id: int, count: int) -> List:
        """Abstract method for create_checker_set"""

    @abstractmethod
    def get_factory_info(self) -> str:
        """Get information about the factory. I hate pylint."""

# CLASS FOR CREATING 30 INSTANCES OF CHECKERS
class CheckerFactory(ICheckerFactory):
    """Abstract class for checker factory"""
    @staticmethod # This allows us to use the method w/o creating an instance of the class.
    def create_checker_set(colour, start_id, count):
        """Creates 15 checkers of each colour"""
        checkers = []
        for i in range(count):
            checkers.append(Checker(start_id + i, colour))
        return checkers

class CheckMoves(IMoveValidator):
    """Class responsible exclusively for validating moves"""

    def __init__(self, board, game):
        self.__board__ = board
        self.__game__ = game

    # ---------- CHECK MOVES -------------
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
        raise InvalidColourError(colour)

    # This method receives the destination point as a parameter.
    # It checks if there are more than 1 opponent checkers in the destination point.
    # It returns True if there are opponent checkers or False if there aren't.
    # This method is a part of the check_move method.
    def check_opponent_checkers(self, destination:str) -> bool:
        """This method checks if there are more than 1 opponent checkers in the destination point"""
        turn = self.__game__.get_turn()
        if turn == "Black":
            if len(self.__board__.get_checkers_in_field(destination)) > 0:
                if self.__board__.get_checkers_in_field(destination)[0].get_colour() == "White":
                    return True
            return False
        if turn == "White":
            if len(self.__board__.get_checkers_in_field(destination)) > 0:
                if self.__board__.get_checkers_in_field(destination)[0].get_colour() == "Black":
                    return True
            return False
        raise InvalidTurnError(turn)

    # This method receives the destination point as a parameter.
    # It checks if there is exactly one opponent checker in the destination point.
    # It returns True if there is exactly one opponent checker or False if there aren't.
    # If there is only one checker, it can be eaten.
    # This method is a part of the check_move method.
    def check_eatable_checker(self, destination:str) -> bool:
        """This method checks if there is exactly one opponent checker in the destination point"""
        turn = self.__game__.get_turn()
        if turn == "Black":
            if len(self.__board__.get_checkers_in_field(str(destination))) == 1:
                if self.__board__.get_checkers_in_field(str(destination))[0].get_colour()=="White":
                    return True
            return False
        if turn == "White":
            if len(self.__board__.get_checkers_in_field(str(destination))) == 1:
                if self.__board__.get_checkers_in_field(str(destination))[0].get_colour()=="Black":
                    return True
            return False
        raise InvalidTurnError(turn)

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
        turn = self.__game__.get_turn()
        if turn == "Black":
            # Check if there are any eaten checkers
            if self.check_eaten_checkers("Black"):
                # Check if the point where the checker has to enter
                # is not blocked by 2 or more white checkers
                return self._check_take_out_with_opponent_checker(str(steps))
            return False
        if turn == "White":
            # Check if there are any eaten checkers
            if self.check_eaten_checkers("White"):
                # Check if the point where the checker has to enter
                # is not blocked by 2 or more black checkers
                return self._check_take_out_with_opponent_checker(str(25 - steps))
            return False
        raise InvalidTurnError(turn)

    # This method receives the origin and the steps as parameters.
    # It checks if a checker can be moved to the house.
    # It returns True if the move is valid. It returns False if:
    # 1. Not all checkers are in the player's square
    # 2. The steps don't match the origin point with the steps to the house
    # AND there are checkers further than the number the steps allow.
    def check_move_to_house(self, origin: str, steps: int) -> bool:
        """Checks if a checker can be moved to the house."""
        turn = self.__game__.get_turn()

        if turn == "Black":
            return self._check_black_move_to_house(origin, steps)
        if turn == "White":
            return self._check_white_move_to_house(origin, steps)
        raise InvalidTurnError(turn)

    # This method receives the origin point and the steps as parameters.
    # It is a sub method of check_move_to_house for black checkers.
    # It returns True if the checker can enter the house. It returns False if it can´t.
    def _check_black_move_to_house(self, origin: str, steps: int) -> bool:
        """Helper method for check_move_to_house in Black case."""
        if origin == "BEaten":
            destination = self.__game__.get_destination_point(origin, steps)
        else:
            destination = self.__game__.get_destination_point(int(origin), steps)

        if int(destination) <= 24:
            return False  # Not a move to the black house

        # Check checkers out of the player's square or eaten checkers
        if self._black_checkers_out_of_square():
            return False

        # Check valid moves to take out checkers
        return self._is_valid_black_bear_off(origin, steps)

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
    # It returns True if the Black player can move a
    # specific checker to the house and false if he/she can't.
    def _is_valid_black_bear_off(self, origin: str, steps: int) -> bool:
        """Check if the specific black checker can be moved to the house."""
        origin_point = int(origin)
        point_to_check = 25 - steps

        # Check if the checker is in the exact point
        if origin_point == point_to_check:
            return True  # Exactly in the point, can be taken out

        # If not in the exact point, check that there are no further checkers
        # Find the FURTHEST checker (highest point in home board)
        lowest_point = 25
        for i_point in range(19, 25):
            if self._black_checker_at_point(i_point):
                lowest_point = min(lowest_point, i_point)

        # Solo puede sacar esta ficha si no hay fichas más lejanas
        return origin_point <= lowest_point

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
        if origin == "WEaten":
            destination = self.__game__.get_destination_point(origin, steps)
        else:
            destination = self.__game__.get_destination_point(int(origin), steps)

        if int(destination) >= 1:
            return False  # Not a move to house

        # Check if there are checkers out of the player's square or eaten checkers
        if self._white_checkers_out_of_square():
            return False

        # Check valid moves to take out checkers
        return self._is_valid_white_bear_off(origin, steps)

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
    def _is_valid_white_bear_off(self, origin:str, steps: int) -> bool:
        """Check if the specific white checker can be moved to the house."""
        origin_point = int(origin)
        point_to_check = steps

        # Check if the checker is in the exact point
        if origin_point == point_to_check:
            return True  # Exactly in the point, can be taken out

        # If not in the exact point, check that there are no further checkers
        # Find the FURTHEST checker (highest point in home board)
        highest_point = 0
        for i_point in range(1, 7): # Check all points in the square
            if self._white_checker_at_point(i_point):
                highest_point = max(highest_point, i_point)

        # Solo puede sacar esta ficha si no hay fichas más lejanas
        return origin_point >= highest_point

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
        destination = self.__game__.get_destination_point(point, steps)

        # First check if there are eaten checkers.
        # If there are, the player must take them out before moving any other checker.
        # First check if there are eaten checkers.
        if self.check_eaten_checkers("Black"):
            # If there are eaten checkers, check if this move is to take one out
            if point == "BEaten":
                return self.check_take_out_eaten_checker(steps)  # Put steps, not colour
            return False  # Cannot move other checkers while having eaten checkers

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
        destination = self.__game__.get_destination_point(point, steps)

        # First check if there are eaten checkers.
        # If there are, the player must take them out before moving any other checker.
        # First check if there are eaten checkers.
        if self.check_eaten_checkers("White"):
            # If there are eaten checkers, check if this move is to take one out
            if point == "WEaten":
                return self.check_take_out_eaten_checker(steps)  # Put steps, not colour
            return False  # Cannot move other checkers while having eaten checkers

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
        turn = self.__game__.get_turn()
        if turn == "Black":
            return self._check_black_move(point, steps)
        if turn == "White":
            return self._check_white_move(point, steps)
        return False # Default

class BackgammonGame:
    """Class with the methods for the logic of the game"""
    # CONSTRUCTOR - sets the main attributes of the class
    def __init__(self,
                 dice: Optional[IDice] = None,
                 move_validator: Optional[IMoveValidator] = None,
                 checker_factory: Optional[ICheckerFactory] = None,
                 player_factory: Optional[Callable[[str, str], IPlayer]] = None):
        # 9 attributes are necessary for the game logic (sorry pylint)
        self.__turn__ = None
        self.__board__ = Board()
        self.__dice1__ = dice if dice is not None else Dice()
        self.__dice2__ = dice if dice is not None else Dice()
        player_creator = player_factory if player_factory is not None else Player
        self.__player1__ = player_creator("Player 1", "White")
        self.__player2__ = player_creator("Player 2", "Black")
        # FIX: instead of making 30 checkers one by one, we use Checker Factory
        # SRP and DIP
        factory = checker_factory if checker_factory is not None else CheckerFactory
        self.__black_checkers__ = factory.create_checker_set("Black", 1, 15)
        self.__white_checkers__ = factory.create_checker_set("White", 16, 15)
        self.__move_validator__ = (move_validator if move_validator is not None
                                   else CheckMoves(self.__board__, self))
        self.__setup_individual_references__()

    def __setup_individual_references__(self):
        """Mantains all the names of the variables of the checkers"""
        # For black checkers
        for i, checker in enumerate(self.__black_checkers__):
            setattr(self, f"__b_{i+1}__", checker)

        # For white checkers
        for i, checker in enumerate(self.__white_checkers__):
            setattr(self, f"__w_{i+1}__", checker)

    # ---------- TURNS -------------
    # SETTERS
    # This method receives the colour of the player as a parameter.
    # It sets 'turn' with the colour of the player whose turn is.
    def set_turn(self, colour):
        """Sets the colour of the player whose turn is"""
        self.__turn__ = colour

    # This method does not receive any parameters.
    # It sets the first turn of the game based on the dice rolls.
    def set_first_turn(self):
        """Sets the first turn of the game based on the dice rolls"""
        first_roll = self.__dice1__.roll()
        second_roll = self.__dice2__.roll()
        while first_roll == second_roll:
            first_roll = self.__dice1__.roll()
            second_roll = self.__dice2__.roll()
        # If the first dice is higher than the second, black starts.
        # If the second dice is higher than the first, white starts.
        if first_roll > second_roll:
            self.set_turn("Black")
        else:
            self.set_turn("White")

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
        raise InvalidTurnError(self.get_turn)

    # METHODS FOR THE GAME

    # SET DEFAULT CHECKERS AT THE BEGINNING OF THE GAME
    # This method does not receive any parameters.
    # It sets the initial position of the checkers on the board.
    # It does not return any value.
    def set_default_checkers(self):
        """Method for setting the initial position of the checkers"""
        # Copy the lists of checkers
        white_checkers = self.__white_checkers__.copy()
        black_checkers = self.__black_checkers__.copy()

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
    # This method receives the point where the chosen checker is and the steps as parameters.
    # It returns True if the move is valid or not.
    # Returns False if the move is not valid. Returns True if the move is valid.
    def check_move(self, point:str, steps:int) -> bool:
        """This method evaluates if the move that is going to be made is valid"""
        return self.__move_validator__.check_move(point, steps)

    # -------------- MAKE MOVES --------------

    # This method receives the origin point and the destination point as parameters.
    # It moves the checker from origin to destination.
    # It does not return any value.
    def move_checker(self, origin:str, steps:int):
        """This method moves the checker from origin to destination"""
        destination = self.get_destination_point(origin, steps)

        # Moves from eaten fields
        if origin in ["Beaten", "WEaten"]:
            if self.__move_validator__.check_take_out_eaten_checker(steps):
                if self.__move_validator__.check_opponent_checkers(destination):
                    if self.__move_validator__.check_eatable_checker(destination):
                        self.eat_opponent_checker(destination)
                checker_to_move = self.__board__.remove_checker_from_field(origin)
                self.__board__.add_checker_to_field(destination, checker_to_move)
            return  # End the method

        # Normal case
        if self.__move_validator__.check_move_to_house(origin, steps):
            if self.get_turn() == "Black":
                destination = "BHouse"
            elif self.get_turn() == "White":
                destination = "WHouse"

        if self.__move_validator__.check_opponent_checkers(destination):
            if self.__move_validator__.check_eatable_checker(destination):
                self.eat_opponent_checker(destination)

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
