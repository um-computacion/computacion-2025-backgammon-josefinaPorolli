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
        expected_checkers = [self.__game__.__b_15__, self.__game__.__b_14__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

        actual_checkers = self.__game__.__board__.get_checkers_in_field("24")
        expected_checkers = [self.__game__.__w_15__, self.__game__.__w_14__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

        # Next set of checkers (nearer to each player's house)
        actual_checkers = self.__game__.__board__.get_checkers_in_field("12")
        expected_checkers = [self.__game__.__b_13__, self.__game__.__b_12__, self.__game__.__b_11__, self.__game__.__b_10__, self.__game__.__b_9__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

        actual_checkers = self.__game__.__board__.get_checkers_in_field("13")
        expected_checkers = [self.__game__.__w_13__, self.__game__.__w_12__, self.__game__.__w_11__, self.__game__.__w_10__, self.__game__.__w_9__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

        # Next set of checkers (nearer to each player's house)
        actual_checkers = self.__game__.__board__.get_checkers_in_field("17")
        expected_checkers = [self.__game__.__b_8__, self.__game__.__b_7__, self.__game__.__b_6__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

        actual_checkers = self.__game__.__board__.get_checkers_in_field("8")
        expected_checkers = [self.__game__.__w_8__, self.__game__.__w_7__, self.__game__.__w_6__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

        # Nearest checkers to each player's house
        actual_checkers = self.__game__.__board__.get_checkers_in_field("19")
        expected_checkers = [self.__game__.__b_5__, self.__game__.__b_4__, self.__game__.__b_3__, self.__game__.__b_2__, self.__game__.__b_1__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

        actual_checkers = self.__game__.__board__.get_checkers_in_field("6")
        expected_checkers = [self.__game__.__w_5__, self.__game__.__w_4__, self.__game__.__w_3__, self.__game__.__w_2__, self.__game__.__w_1__]
        actual_ids = [checker.get_id() for checker in actual_checkers]
        expected_ids = [checker.get_id() for checker in expected_checkers]
        self.assertEqual(actual_ids, expected_ids)

    def test_check_winner(self):
        # Check that there is no winner at first
        self.assertEqual("None", self.__game__.check_winner())

        # Simulate all white checkers in their house
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_1__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_2__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_3__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_4__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_5__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_6__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_7__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_8__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_9__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_10__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_11__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_12__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_13__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_14__)
        self.__game__.__board__.add_checker_to_field("WHouse", self.__game__.__w_15__)
        self.assertEqual("White", self.__game__.check_winner())

        # Remove a checker from the white house
        self.__game__.__board__.remove_checker_from_field("WHouse")
        # Simulate all black checkers in their house
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_1__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_2__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_3__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_4__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_5__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_6__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_7__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_8__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_9__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_10__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_11__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_12__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_13__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_14__)
        self.__game__.__board__.add_checker_to_field("BHouse", self.__game__.__b_15__)
        self.assertEqual("Black", self.__game__.check_winner())

    def test_get_destination_point(self):
        # Test for black checkers
        # 1. Set the turn to Black
        self.__game__.set_turn("Black")
        # 2. Add a black checker to any point (e.g., point 8, BEaten)
        self.__game__.__board__.add_checker_to_field("8", self.__game__.__b_1__)
        self.__game__.__board__.add_checker_to_field("BEaten", self.__game__.__b_2__)
        # As the dice roll is random, we will set the number of steps directly to 6.
        self.assertEqual(self.__game__.get_destination_point("8", 6), "14")
        self.assertEqual(self.__game__.get_destination_point("BEaten", 6), "6")

        # Test for white checkers
        # 1. Set the turn to White
        self.__game__.set_turn("White")
        # 2. Add a white checker to any point (e.g., point 3, WEaten)
        self.__game__.__board__.add_checker_to_field("3", self.__game__.__w_1__)
        self.__game__.__board__.add_checker_to_field("WEaten", self.__game__.__w_2__)
        # As the dice roll is random, we will set the number of steps directly to 6.
        self.assertEqual(self.__game__.get_destination_point("3", 6), "-3")
        self.assertEqual(self.__game__.get_destination_point("WEaten", 6), "19")

    def test_eaten_checkers(self):
        # At first, the spaces for eaten checkers are empty
        self.assertFalse(self.__game__.check_eaten_checkers("White"))
        self.assertFalse(self.__game__.check_eaten_checkers("Black"))
        # Add checkers to the "eaten" spaces
        self.__game__.__board__.add_checker_to_field("BEaten", self.__game__.__b_1__)
        self.__game__.__board__.add_checker_to_field("WEaten", self.__game__.__w_1__)
        # Now the method should return True
        self.assertTrue(self.__game__.check_eaten_checkers("White"))
        self.assertTrue(self.__game__.check_eaten_checkers("Black"))

    def test_check_opponent_checkers(self):
        # Test for black turn
        self.__game__.set_turn("Black")
        # There should not be any checkers in any point, so an arbitrary one should return false
        self.assertFalse(self.__game__.check_opponent_checkers("4"))
        # Add a white checker to point 4
        self.__game__.__board__.add_checker_to_field("4", self.__game__.__w_1__)
        # Now the method should return true in that point
        self.assertTrue(self.__game__.check_opponent_checkers("4"))

        # Test for white turn
        self.__game__.set_turn("White")
        # There should not be any checkers in any point
        # (except 4 because we added a white one before), so an arbitrary one should return false
        self.assertFalse(self.__game__.check_opponent_checkers("20"))
        # Add a white checker to point 20
        self.__game__.__board__.add_checker_to_field("20", self.__game__.__b_1__)
        # Now the method should return true in that point
        self.assertTrue(self.__game__.check_opponent_checkers("20"))

    def test_check_eatable_checker(self):
        # Test for black turn
        self.__game__.set_turn("Black")
        # There should not be any checkers in any point, so an arbitrary one should return false
        self.assertFalse(self.__game__.check_eatable_checker("4"))
        # Add a white checker to point 4
        self.__game__.__board__.add_checker_to_field("4", self.__game__.__w_1__)
        # Now the method should return true in that point, as there is only one checker in point 4
        self.assertTrue(self.__game__.check_eatable_checker("4"))
        # Add another white checker to point 4
        self.__game__.__board__.add_checker_to_field("4", self.__game__.__w_2__)
        # Now the method should return false in that point as there is more than one checker in point 4
        self.assertFalse(self.__game__.check_eatable_checker("4"))

        # Test for white turn
        self.__game__.set_turn("White")
        # There should not be any checkers in any point
        # (except 4 because we added white ones before), so an arbitrary one should return false
        self.assertFalse(self.__game__.check_eatable_checker("20"))
        # Add a black checker to point 20, as there is only one checker in point 20
        self.__game__.__board__.add_checker_to_field("20", self.__game__.__b_1__)
        # Now the method should return true in that point
        self.assertTrue(self.__game__.check_eatable_checker("20"))
        # Add another black checker to point 20
        self.__game__.__board__.add_checker_to_field("20", self.__game__.__b_2__)
        # Now the method should return false in that point as there is more than one checker in point 20
        self.assertFalse(self.__game__.check_eatable_checker("20"))

    def test_check_take_out_eaten_checker(self):
        # At first, there will be no eaten checkers.
        # Set each turn and the method with an arbitrary number of steps (3) should return False
        self.__game__.set_turn("Black")
        self.assertFalse(self.__game__.check_take_out_eaten_checker(3))
        self.__game__.set_turn("White")
        self.assertFalse(self.__game__.check_take_out_eaten_checker(3))

        # Add checkers to the eaten fileds but not to the destination. The method should return false.
        self.__game__.__board__.add_checker_to_field("BEaten", self.__game__.__b_1__)
        self.__game__.set_turn("Black")
        self.assertTrue(self.__game__.check_take_out_eaten_checker(3))
        self.__game__.__board__.add_checker_to_field("WEaten", self.__game__.__w_1__)
        self.__game__.set_turn("White")
        self.assertTrue(self.__game__.check_take_out_eaten_checker(3))

        # Add one opponent checker to each destination point.
        # The player should be able to eat the checker and the method should return True.
        self.__game__.__board__.add_checker_to_field("3", self.__game__.__w_2__)
        self.__game__.set_turn("Black")
        self.assertTrue(self.__game__.check_take_out_eaten_checker(3))
        self.__game__.__board__.add_checker_to_field("22", self.__game__.__b_2__)
        self.__game__.set_turn("White")
        self.assertTrue(self.__game__.check_take_out_eaten_checker(3))

        # Add another opponent checker to each destination point.
        # The method should now return False
        # Add one opponent checker to each destination point.
        # The player should be able to eat the checker and the method should return True.
        self.__game__.__board__.add_checker_to_field("3", self.__game__.__w_3__)
        self.__game__.set_turn("Black")
        self.assertFalse(self.__game__.check_take_out_eaten_checker(3))
        self.__game__.__board__.add_checker_to_field("22", self.__game__.__b_3__)
        self.__game__.set_turn("White")
        self.assertFalse(self.__game__.check_take_out_eaten_checker(3))

    def test_check_move_to_house(self):
        # Add just one checker to the player's final square In this case, in the middle of it.
        self.__game__.__board__.add_checker_to_field("22", self.__game__.__b_1__)
        self.__game__.__board__.add_checker_to_field("3", self.__game__.__w_1__)
        # If the steps are larger or equal to the required steps, it should return True.
        self.__game__.set_turn("Black")
        self.assertTrue(self.__game__.check_move_to_house("22", 3))
        self.assertTrue(self.__game__.check_move_to_house("22", 4))
        # If not, it should return False. 
        self.assertFalse(self.__game__.check_move_to_house("22", 2))
        # Same case with white
        self.__game__.set_turn("White")
        self.assertTrue(self.__game__.check_move_to_house("3", 3))
        self.assertTrue(self.__game__.check_move_to_house("3", 4))
        # If not, it should return False. 
        self.assertFalse(self.__game__.check_move_to_house("3", 2))

        # Add a checker further than the selected one
        self.__game__.__board__.add_checker_to_field("21", self.__game__.__b_2__)
        self.__game__.__board__.add_checker_to_field("4", self.__game__.__w_2__)
        # As there are further checkers, it should return false.
        self.__game__.set_turn("Black")
        self.assertFalse(self.__game__.check_move_to_house("22", 2))
        self.__game__.set_turn("White")
        self.assertFalse(self.__game__.check_move_to_house("3", 2))

        # Add checkers out of each player's squares
        self.__game__.__board__.add_checker_to_field("8", self.__game__.__b_3__)
        self.__game__.__board__.add_checker_to_field("9", self.__game__.__w_3__)
        # As there are checkers out of the squares, it should return false.
        self.__game__.set_turn("Black")
        self.assertFalse(self.__game__.check_move_to_house("22", 2))
        self.__game__.set_turn("White")
        self.assertFalse(self.__game__.check_move_to_house("3", 2))

        # Remove the checkers b2 and w2 to test only checkers out of the square
        self.__game__.__board__.remove_checker_from_field("21")
        self.__game__.__board__.remove_checker_from_field("4")
        # As there are further checkers, it should return false.
        self.__game__.set_turn("Black")
        self.assertFalse(self.__game__.check_move_to_house("22", 2))
        self.__game__.set_turn("White")
        self.assertFalse(self.__game__.check_move_to_house("3", 2))
    
    def test_check_move(self):
        # Add checkers to random points
        self.__game__.__board__.add_checker_to_field("22", self.__game__.__b_1__)
        self.__game__.__board__.add_checker_to_field("3", self.__game__.__w_1__)
        self.__game__.__board__.add_checker_to_field("21", self.__game__.__b_2__)
        self.__game__.__board__.add_checker_to_field("4", self.__game__.__w_2__)
        self.__game__.__board__.add_checker_to_field("8", self.__game__.__b_3__)
        self.__game__.__board__.add_checker_to_field("9", self.__game__.__w_3__)

        # Black's turn
        self.__game__.set_turn("Black")
        # Check a valid move with no eaten checkers. Should return True.
        self.assertTrue(self.__game__.check_move("21", 1))
        self.assertTrue(self.__game__.check_move("22", 1))
        # Add a checker to the BEaten field
        self.__game__.__board__.add_checker_to_field("BEaten", self.__game__.__b_4__)
        # Now the method should return False
        self.assertFalse(self.__game__.check_move("21", 1)) # DOES NOT PASS. CHECK.

if __name__ == "__main__":
    unittest.main() 
