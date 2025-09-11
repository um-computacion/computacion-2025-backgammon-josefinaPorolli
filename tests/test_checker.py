"""Test module for methods in class Checker"""

import unittest
from core.checker import Checker

class TestChecker(unittest.TestCase):
    def setUp(self):
        self.checker = Checker("Black")

    def test_get_id(self):
        """Test for getting the checker id."""
        # As we do not know the id (depends on memory address), we just make sure the type is correct
        self.assertIsInstance(self.checker.get_id(), int)

    def test_get_colour(self):
        """Test for making sure the colour of the checker is correct."""
        # As we set the color to Black in setUp, we check if it's correct
        self.assertEqual(self.checker.get_colour(), "Black")
    
    def test_set_colour(self):
        """Test for setting the checker colour."""
        self.checker.set_colour("White") # Change the colour to white
        self.assertEqual(self.checker.get_colour(), "White") # Check if the colour has been changed correctly

if __name__ == "__main__":
    unittest.main()