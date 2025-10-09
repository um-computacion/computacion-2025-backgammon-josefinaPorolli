"""Module for testing the Backgammon Game class"""
import unittest
from core.backgammon_game import BackgammonGame

class testBackgammonGame(unittest.TestCase):
    """Test for methods in class BackgammonGame"""
    def setUp(self):
        self.__game__ = BackgammonGame()

    def test_set_and_get_turn(self):
        self.__game__.set_turn("Black")
        self.assertEqual(self.__game__.get_turn(), "Black")
        self.__game__.set_turn("White")
        self.assertEqual(self.__game__.get_turn(), "White")

    def test_set_default_checkers(self):
        self.__game__.set_default_checkers()

        # Furthest checkers to each player's house
        actual_checkers = self.__game__.__board__.get_checkers_in_field("1")
        expected_checkers = [self.__game__.__B_15__, self.__game__.__B_14__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

        actual_checkers = self.__game__.__board__.get_checkers_in_field("24")
        expected_checkers = [self.__game__.__W_15__, self.__game__.__W_14__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

        # Next set of checkers (nearer to each player's house)
        actual_checkers = self.__game__.__board__.get_checkers_in_field("12")
        expected_checkers = [self.__game__.__B_13__, self.__game__.__B_12__, self.__game__.__B_11__, self.__game__.__B_10__, self.__game__.__B_9__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

        actual_checkers = self.__game__.__board__.get_checkers_in_field("13")
        expected_checkers = [self.__game__.__W_13__, self.__game__.__W_12__, self.__game__.__W_11__, self.__game__.__W_10__, self.__game__.__W_9__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

        # Next set of checkers (nearer to each player's house)
        actual_checkers = self.__game__.__board__.get_checkers_in_field("17")
        expected_checkers = [self.__game__.__B_8__, self.__game__.__B_7__, self.__game__.__B_6__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

        actual_checkers = self.__game__.__board__.get_checkers_in_field("8")
        expected_checkers = [self.__game__.__W_8__, self.__game__.__W_7__, self.__game__.__W_6__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

        # Nearest checkers to each player's house
        actual_checkers = self.__game__.__board__.get_checkers_in_field("19")
        expected_checkers = [self.__game__.__B_5__, self.__game__.__B_4__, self.__game__.__B_3__, self.__game__.__B_2__, self.__game__.__B_1__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

        actual_checkers = self.__game__.__board__.get_checkers_in_field("6")
        expected_checkers = [self.__game__.__W_5__, self.__game__.__W_4__, self.__game__.__W_3__, self.__game__.__W_2__, self.__game__.__W_1__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

    def test_check_winner(self):
        # Check that there is no winner at first
        self.assertEqual("None", self.__game__.check_winner())

        # Simulate all white checkers in their house
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_1__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_2__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_3__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_4__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_5__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_6__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_7__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_8__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_9__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_10__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_11__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_12__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_13__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_14__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__W_15__)
        self.assertEqual("White", self.__game__.check_winner())

        # Remove a checker from the white house
        self.__game__.__board__.remove_checker_from_field("WHouse")
        # Simulate all black checkers in their house
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_1__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_2__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_3__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_4__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_5__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_6__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_7__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_8__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_9__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_10__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_11__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_12__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_13__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_14__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__B_15__)
        self.assertEqual("Black", self.__game__.check_winner())

if __name__ == "__main__":
    unittest.main() 
