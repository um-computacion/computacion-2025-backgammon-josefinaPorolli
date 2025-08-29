import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):
    # First create an object for the Player class. Juan Pedro would be playing with the Black checkers
    def setUp(self):
        self.player = Player("Juan Pedro", "Black")
    
    # Test every method included in the class
    # Getters
    def test_get_name(self): # returns the player's name
        self.assertEqual(self.player.get_name(), "Juan Pedro")

    def test_get_colour(self): # returns the player's colour
        self.assertEqual(self.player.get_colour(), "Black")

    def test_set_name(self): # updates the player's name
        self.player.set_name("Peppa Pig")
        self.assertEqual(self.player.get_name(), "Peppa Pig")

    def test_set_colour(self):
        self.player.set_colour("White")
        self.assertEqual(self.player.get_colour(), "White")

if __name__ == "__main__":
    unittest.main()

