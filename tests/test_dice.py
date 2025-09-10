"""Test module for methods in class Dice"""

import unittest
from core.dice import Dice

class TestDice(unittest.TestCase):
    """Test class for Dice methods."""
    def setUp(self):
        self.dice = Dice()

    # Test for getting the current number of the dice
    def test_get_number(self):
        """Test for getting the current number of the dice."""
        self.assertIsNone(self.dice.get_number()) # Initial value of the dice
        self.dice.roll() # roll the dice to get a valid number
        self.assertIn(self.dice.get_number(), self.dice.__values__) # Check if the value is valid

    # Test for rolling the dice
    def test_roll_dice(self):
        """Test for rolling the dice."""
        result = self.dice.roll() # "Roll" the dice
        # As the result is going to be a random number, we check if it is valid.
        self.assertIn(result, self.dice.__values__)

if __name__ == "__main__":
    unittest.main()
