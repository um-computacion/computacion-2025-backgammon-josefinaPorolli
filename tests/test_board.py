"""Test module for methods in class Checker"""

import unittest
from core.board import Board
from core.checker import Checker

class TestBoard(unittest.TestCase):
    """Test for methods in class Checker"""
    def setUp(self):
        self.__board__ = Board()
        self.__b_1__ = Checker(1, "Black")
        self.__b_2__ = Checker(2, "Black")
        self.__w_1__ = Checker(3, "White")
        self.__w_2__ = Checker(4, "White")

    def test_get_board(self):
        """Test form method that returns all the points of the board"""
        self.assertEqual(self.__board__.get_board(),
        {"1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": [],
        "10": [],
        "11": [],
        "12": [],
        "13": [],
        "14": [],
        "15": [],
        "16": [],
        "17": [],
        "18": [],
        "19": [],
        "20": [],
        "21": [],
        "22": [],
        "23": [],
        "24": [],
        "BHouse": [],
        "WHouse": [],
        "BEaten": [],
        "WEaten": []})

    def test_get_checkers_in_field(self):
        """Test for method about getting all the checkers in a spescific field."""
        # Many examples were taken. As everything is empty, all the points are in the same state.
        self.assertEqual(self.__board__.get_checkers_in_field("1"), [])
        self.assertEqual(self.__board__.get_checkers_in_field("2"), [])
        self.assertEqual(self.__board__.get_checkers_in_field("3"), [])
        self.assertEqual(self.__board__.get_checkers_in_field("4"), [])
        self.assertEqual(self.__board__.get_checkers_in_field("24"), [])
        self.assertEqual(self.__board__.get_checkers_in_field("23"), [])
        self.assertEqual(self.__board__.get_checkers_in_field("22"), [])
        self.assertEqual(self.__board__.get_checkers_in_field("21"), [])
        self.assertEqual(self.__board__.get_checkers_in_field("BHouse"), [])
        self.assertEqual(self.__board__.get_checkers_in_field("WHouse"), [])

    def test_add_checker_to_field(self):
        """Test for method about adding a checker to a field"""
        # Use the function
        self.__board__.add_checker_to_field("1", self.__b_1__)
        self.__board__.add_checker_to_field("1", self.__b_2__)
        self.__board__.add_checker_to_field("5", self.__w_1__)
        self.__board__.add_checker_to_field("6", self.__w_2__)
        # Test the points that now should have checkers in them
        self.assertEqual(self.__board__.get_checkers_in_field("1"), [self.__b_1__, self.__b_2__])
        self.assertEqual(self.__board__.get_checkers_in_field("5"), [self.__w_1__])
        self.assertEqual(self.__board__.get_checkers_in_field("6"), [self.__w_2__])
        # Test the points that should be empty
        self.assertEqual(self.__board__.get_checkers_in_field("2"), [])
        self.assertEqual(self.__board__.get_checkers_in_field("3"), [])
        self.assertEqual(self.__board__.get_checkers_in_field("4"), [])
        self.assertEqual(self.__board__.get_checkers_in_field("BHouse"), [])
        self.assertEqual(self.__board__.get_checkers_in_field("WEaten"), [])
        # Test the whole board
        self.assertEqual(self.__board__.get_board(),
        {"1": [self.__b_1__, self.__b_2__],
        "2": [],
        "3": [],
        "4": [],
        "5": [self.__w_1__],
        "6": [self.__w_2__],
        "7": [],
        "8": [],
        "9": [],
        "10": [],
        "11": [],
        "12": [],
        "13": [],
        "14": [],
        "15": [],
        "16": [],
        "17": [],
        "18": [],
        "19": [],
        "20": [],
        "21": [],
        "22": [],
        "23": [],
        "24": [],
        "BHouse": [],
        "WHouse": [],
        "BEaten": [],
        "WEaten": []})

    def test_remove_checker_from_field(self):
        """Test for method about removing a checker from a field"""
        # First add some checkers to a field
        self.__board__.add_checker_to_field("1", self.__b_1__)
        self.__board__.add_checker_to_field("1", self.__b_2__)
        # Try to remove those checkers from the field
        self.__board__.remove_checker_from_field("1")
        # Test the result
        self.assertEqual(self.__board__.get_checkers_in_field("1"), [self.__b_1__])

if __name__ == "__main__":
    unittest.main()
