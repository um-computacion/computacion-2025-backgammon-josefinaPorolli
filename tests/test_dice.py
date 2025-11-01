"""Test module for methods in class Dice"""

import unittest
from unittest.mock import patch
from core.dice import Dice

class TestDice(unittest.TestCase):
    """Test class for Dice methods."""

    def setUp(self):
        self.dice = Dice()

    # Test for getting the initial value before rolling anything
    def test_get_number_initial(self):
        """Test that initial dice value is None."""
        self.assertIsNone(self.dice.get_number())

    # Test the setter of the values (roll)
    @patch('random.randint')
    def test_roll(self, mock_randint):
        """Test that roll() sets the current value correctly."""
        mock_randint.return_value = 4 # We force the value with mock

        result = self.dice.roll()

        # Test that roll() returns the correct value
        self.assertEqual(result, 4)
        # Test that get_number() returns the same value after roll
        self.assertEqual(self.dice.get_number(), 4)
        # Verify randint was called with correct parameters
        mock_randint.assert_called_once_with(1, 6)

    # Test fot getter
    @patch('random.randint')
    def test_get_number(self, mock_randint):
        """Test that get_number() returns the value set by roll()."""
        mock_randint.return_value = 3

        self.dice.roll()
        result = self.dice.get_number()

        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
