import unittest
from core.dice import Dice

class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()

    # Test for getting the current number of the dice
    def test_get_number(self):
        self.assertIsNone(self.dice.get_number()) # Initial value of the dice
        self.dice.roll() # roll the dice to get a valid number
        self.assertIn(self.dice.get_number(), self.dice.__values__) # Check if the returned value is valid
    
    # Test for rolling the dice
    def test_roll_dice(self):
        result = self.dice.roll() # "Roll" the dice
        self.assertIn(result, self.dice.__values__) # As the result is going to be a random number (we do not know which), we check if it is valid so that the test returns a successful value.
    
if __name__ == "__main__":
    unittest.main()
