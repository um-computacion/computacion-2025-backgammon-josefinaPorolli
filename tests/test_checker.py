"""Test module for methods in class Checker"""

import unittest
from core.checker import Checker

class TestChecker(unittest.TestCase):
    def setUp(self):
        self.checker = Checker(1, "Black") # First 15 checkers are black, next 15 are white

    def test_get_id(self):
        """Test for getting the checker id."""
        # As we set the id to 1 in setUp, we check if it's correct
        self.assertEqual(self.checker.get_id(), 1)

    def test_get_colour(self):
        """Test for making sure the colour of the checker is correct."""
        # As we set the color to Black in setUp, we check if it's correct
        self.assertEqual(self.checker.get_colour(), "Black")

if __name__ == "__main__":
    unittest.main()
    