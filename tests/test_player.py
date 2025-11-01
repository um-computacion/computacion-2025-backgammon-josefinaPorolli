"""Test module for methods in class Player"""

import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):
    """Test class for Player methods."""
    # First create an object for the Player class.
    # Juan Pedro would be playing with the Black checkers
    def setUp(self):
        self.player = Player("Juan Pedro", "Black")

    # Test every method included in the class
    # Getters
    def test_get_name(self):
        """Test for getting the player's name."""
        self.assertEqual(self.player.get_name(), "Juan Pedro")

    def test_get_colour(self):
        """Test for getting the player's colour."""
        self.assertEqual(self.player.get_colour(), "Black")

    def test_set_name(self):
        """Test for setting the player's name."""
        self.player.set_name("Peppa Pig")
        self.assertEqual(self.player.get_name(), "Peppa Pig")

    def test_set_colour(self):
        """Test for setting the player's colour."""
        self.player.set_colour("White")
        self.assertEqual(self.player.get_colour(), "White")

if __name__ == "__main__":
    unittest.main()
