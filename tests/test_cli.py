import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from cli.cli import BackgammonCLI


class TestBackgammonCLI(unittest.TestCase):
    """Test suite for BackgammonCLI"""

    def setUp(self):
        """Set up test fixtures"""
        self.cli = BackgammonCLI()

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_dice_roll_normal(self, mock_stdout):
        """It should display normal dice roll results.

        Args:
            mock_stdout: Mock for stdout to capture print output
        """
        # Arrange: Patch dice getters to return specific values
        with patch.object(
            self.cli.game.__dice1__, "get_number", return_value=3
        ), patch.object(self.cli.game.__dice2__, "get_number", return_value=5):
            # Act: Display dice roll
            self.cli.display_dice_roll()

        # Assert

        # Assert: Check output contains dice values
        output = mock_stdout.getvalue()
        self.assertIn("Dice Roll: 3 and 5", output)
        self.assertNotIn("DOUBLES", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_dice_roll_doubles(self, mock_stdout):
        """It should display doubles message when dice match.

        Args:
            mock_stdout: Mock for stdout to capture print output
        """
        # Arrange: Patch matching dice values
        with patch.object(
            self.cli.game.__dice1__, "get_number", return_value=4
        ), patch.object(self.cli.game.__dice2__, "get_number", return_value=4):
            # Act: Display dice roll
            self.cli.display_dice_roll()

        # Assert

        # Assert: Check output contains doubles message
        output = mock_stdout.getvalue()
        self.assertIn("Dice Roll: 4 and 4", output)
        self.assertIn("DOUBLES!", output)
        self.assertIn("4 moves", output)

    @patch("builtins.input")
    def test_get_player_names_valid_input(self, mock_input):
        """It should accept valid player names.

        Args:
            mock_input: Mock for input function
        """
        # Arrange: Mock valid inputs
        mock_input.side_effect = ["Alice", "Bob"]

        # Act: Get player names
        black_name, white_name = self.cli.get_player_names()

        # Assert: Check names were set correctly
        self.assertEqual(black_name, "Alice")
        self.assertEqual(white_name, "Bob")
        self.assertEqual(self.cli.game.__player1__.get_name(), "Alice")
        self.assertEqual(self.cli.game.__player2__.get_name(), "Bob")

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_player_names_rejects_empty(self, mock_stdout, mock_input):
        """It should reject empty names and prompt again.

        Args:
            mock_stdout: Mock for stdout to capture print output
            mock_input: Mock for input function
        """
        # Arrange: Mock empty inputs followed by valid ones
        mock_input.side_effect = ["", "Alice", "", "  ", "Bob"]

        # Act: Get player names
        black_name, white_name = self.cli.get_player_names()

        # Assert: Check names were eventually set
        self.assertEqual(black_name, "Alice")
        self.assertEqual(white_name, "Bob")

        # Assert: Check error messages were shown
        output = mock_stdout.getvalue()
        self.assertIn("Name cannot be empty", output)

    @patch("os.system")
    def test_clear_screen_windows(self, mock_system):
        """It should call 'cls' on Windows systems.

        Args:
            mock_system: Mock for os.system function
        """
        # Arrange: Mock Windows environment
        with patch("os.name", "nt"):
            # Act: Clear screen
            self.cli.clear_screen()

            # Assert: Check correct command was called
            mock_system.assert_called_once_with("cls")

    @patch("os.system")
    def test_clear_screen_unix(self, mock_system):
        """It should call 'clear' on Unix systems.

        Args:
            mock_system: Mock for os.system function
        """
        # Arrange: Mock Unix environment
        with patch("os.name", "posix"):
            # Act: Clear screen
            self.cli.clear_screen()

            # Assert: Check correct command was called
            mock_system.assert_called_once_with("clear")

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_determine_first_turn_white_wins(self, mock_stdout, mock_input):
        """It should determine White goes first when White wins el dado."""
        self.cli.game.__player1__.set_name("Alice")
        self.cli.game.__player2__.set_name("Bob")

        def stub_set_first_turn_white():
            self.cli.game.set_turn("White")

        with patch.object(
            self.cli.game, "set_first_turn", side_effect=stub_set_first_turn_white
        ), patch.object(
            self.cli.game.__dice1__, "get_number", return_value=2
        ), patch.object(
            self.cli.game.__dice2__, "get_number", return_value=6
        ):
            self.cli.determine_first_turn()

        output = mock_stdout.getvalue()
        self.assertIn("Black rolled: 2", output)
        self.assertIn("White rolled: 6", output)
        self.assertIn("Bob goes first", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_dice_roll_no_doubles(self, mock_stdout):
        """It should not print doubles when los valores difieren."""
        with patch.object(
            self.cli.game.__dice1__, "get_number", return_value=1
        ), patch.object(self.cli.game.__dice2__, "get_number", return_value=2):
            self.cli.display_dice_roll()
        output = mock_stdout.getvalue()
        self.assertIn("Dice Roll: 1 and 2", output)
        self.assertNotIn("DOUBLES", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_play_game_winner_flow(self, mock_stdout, mock_input):
        """It should hit winner branch and break el loop principal."""
        # Names
        mock_input.side_effect = ["Alice", "Bob", "", ""]

        with patch.object(self.cli, "clear_screen"), patch.object(
            self.cli, "determine_first_turn"
        ), patch.object(self.cli.game, "set_default_checkers"), patch.object(
            self.cli.game, "check_winner", side_effect=["Black"]
        ):
            self.cli.play_game()

        output = mock_stdout.getvalue()
        self.assertIn("CONGRATULATIONS", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_player_move_value_error_then_success(self, mock_stdout, mock_input):
        """It should handle ValueError en steps y luego aceptar valores válidos."""
        self.cli.game.set_default_checkers()
        self.cli.game.set_turn("Black")
        available_moves = [3, 5]
        mock_input.side_effect = [
            "1",  # valid origin
            "abc",  # steps causa ValueError
            "1",  # valid origin again
            "3",  # valid steps
        ]
        with patch.object(self.cli.game, "check_move", return_value=True):
            origin, steps = self.cli.get_player_move("Alice", "Black", available_moves)
        output = mock_stdout.getvalue()
        self.assertIn("Please enter valid input!", output)
        self.assertEqual(origin, "1")
        self.assertEqual(steps, 3)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_player_move_generic_exception_then_success(
        self, mock_stdout, mock_input
    ):
        """It should handle Exception genérica y continuar pidiendo datos."""
        self.cli.game.set_default_checkers()
        self.cli.game.set_turn("Black")
        available_moves = [3, 5]
        mock_input.side_effect = [
            "1",  # origin (will trigger exception path first)
            "1",  # origin again
            "3",  # steps
        ]

        original_get_board = self.cli.game.__board__.get_board

        def flaky_get_board():
            # Raise once, then behave normally
            self.cli.game.__board__.get_board = original_get_board
            raise Exception("boom")

        with patch.object(
            self.cli.game.__board__, "get_board", side_effect=flaky_get_board
        ), patch.object(self.cli.game, "check_move", return_value=True):
            origin, steps = self.cli.get_player_move("Alice", "Black", available_moves)
        output = mock_stdout.getvalue()
        self.assertIn("Error: boom", output)
        self.assertEqual(origin, "1")
        self.assertEqual(steps, 3)

    @patch("sys.stdout", new_callable=StringIO)
    def test_main_keyboard_interrupt(self, mock_stdout):
        """It should manejar KeyboardInterrupt en main sin fallar."""
        with patch("cli.cli.BackgammonCLI.play_game", side_effect=KeyboardInterrupt()):
            from cli.cli import main

            main()
        output = mock_stdout.getvalue()
        self.assertIn("Game interrupted", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_main_generic_exception(self, mock_stdout):
        """It should manejar Exception genérica en main y mostrar mensaje."""
        with patch("cli.cli.BackgammonCLI.play_game", side_effect=Exception("x")):
            from cli.cli import main

            main()
        output = mock_stdout.getvalue()
        self.assertIn("An error occurred", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_main_normal(self, mock_stdout):
        """It should ejecutar main normal llamando a play_game."""
        with patch("cli.cli.BackgammonCLI.play_game") as pg:
            from cli.cli import main

            main()
            pg.assert_called_once()

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_play_game_one_iteration_with_moves(self, mock_stdout, mock_input):
        """It should recorrer una iteración completa con movimientos no dobles."""
        # Avoid blocking inputs between screens
        mock_input.return_value = ""

        with patch.object(
            self.cli, "get_player_names", return_value=("Alice", "Bob")
        ), patch.object(self.cli, "clear_screen"), patch.object(
            self.cli, "display_board"
        ), patch.object(
            self.cli,
            "determine_first_turn",
            side_effect=lambda: self.cli.game.set_turn("Black"),
        ), patch.object(
            self.cli.game, "check_winner", side_effect=["None", "Black"]
        ), patch.object(
            self.cli.game.__dice1__, "roll", return_value=3
        ), patch.object(
            self.cli.game.__dice2__, "roll", return_value=5
        ), patch.object(
            self.cli.game.__dice1__, "get_number", return_value=3
        ), patch.object(
            self.cli.game.__dice2__, "get_number", return_value=5
        ), patch.object(
            self.cli.game, "check_move", return_value=True
        ), patch.object(
            self.cli.game, "move_checker"
        ):
            # Provide two moves consumed sequentially
            with patch.object(
                self.cli, "get_player_move", side_effect=[("1", 3), ("1", 5)]
            ):
                self.cli.play_game()

        output = mock_stdout.getvalue()
        self.assertIn("Alice's turn (Black)", output)
        self.assertIn("Remaining moves: [3, 5]", output)
        self.assertIn("CONGRATULATIONS", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_play_game_doubles_no_valid_moves(self, mock_stdout, mock_input):
        """It should manejar dobles y no movimientos válidos, mostrando mensaje y continuar."""
        mock_input.return_value = ""

        with patch.object(
            self.cli, "get_player_names", return_value=("Alice", "Bob")
        ), patch.object(self.cli, "clear_screen"), patch.object(
            self.cli, "display_board"
        ), patch.object(
            self.cli,
            "determine_first_turn",
            side_effect=lambda: self.cli.game.set_turn("Black"),
        ), patch.object(
            self.cli.game, "check_winner", side_effect=["None", "Black"]
        ), patch.object(
            self.cli.game.__dice1__, "roll", return_value=4
        ), patch.object(
            self.cli.game.__dice2__, "roll", return_value=4
        ), patch.object(
            self.cli.game.__dice1__, "get_number", return_value=4
        ), patch.object(
            self.cli.game.__dice2__, "get_number", return_value=4
        ), patch.object(
            self.cli.game, "check_move", return_value=False
        ):
            # get_player_move should never be called since no valid moves
            self.cli.play_game()

        output = mock_stdout.getvalue()
        self.assertIn("has no valid moves available", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_determine_first_turn_black_wins(self, mock_stdout):
        """It should determine Black player goes first when rolling higher.

        Args:
            mock_stdout: Mock for stdout to capture print output
            mock_roll: Mock for dice roll method
        """
        # Arrange: Set player names and mock rolls
        self.cli.game.__player1__.set_name("Alice")
        self.cli.game.__player2__.set_name("Bob")

        # Stub set_first_turn to set dice values and Black turn
        def stub_set_first_turn():
            # Ensure get_number returns expected values for the printout
            self.cli.game.set_turn("Black")

        with patch.object(
            self.cli.game, "set_first_turn", side_effect=stub_set_first_turn
        ), patch.object(
            self.cli.game.__dice1__, "get_number", return_value=5
        ), patch.object(
            self.cli.game.__dice2__, "get_number", return_value=3
        ), patch(
            "builtins.input"
        ):
            # Act
            self.cli.determine_first_turn()

        # Assert: Check Black won and goes first
        output = mock_stdout.getvalue()
        self.assertIn("Black rolled: 5", output)
        self.assertIn("White rolled: 3", output)
        self.assertIn("Alice goes first", output)
        self.assertEqual(self.cli.game.get_turn(), "Black")

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_player_move_invalid_origin(self, mock_stdout, mock_input):
        """It should reject invalid origin points.

        Args:
            mock_stdout: Mock for stdout to capture print output
            mock_input: Mock for input function
        """
        # Arrange: Setup game state
        self.cli.game.set_default_checkers()
        self.cli.game.set_turn("Black")
        available_moves = [3, 5]

        # Mock inputs: invalid point -> valid move
        mock_input.side_effect = [
            "999",  # Invalid point
            "3",  # Invalid - no checkers
            "1",  # Valid origin
            "3",  # Valid steps
        ]

        # Act: Get player move
        origin, steps = self.cli.get_player_move("Alice", "Black", available_moves)

        # Assert: Check validation messages and final valid move
        output = mock_stdout.getvalue()
        self.assertIn("Invalid origin", output)
        self.assertEqual(origin, "1")
        self.assertEqual(steps, 3)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_player_move_valid_flow(self, mock_stdout, mock_input):
        """It should accept a valid origin/steps and return them."""
        # Arrange
        self.cli.game.set_default_checkers()
        self.cli.game.set_turn("Black")
        available_moves = [3, 5]
        # Choose origin with black checker and valid steps
        mock_input.side_effect = ["1", "3"]

        # To ensure move is valid, mock check_move True
        with patch.object(self.cli.game, "check_move", return_value=True):
            origin, steps = self.cli.get_player_move("Alice", "Black", available_moves)

        self.assertEqual(origin, "1")
        self.assertEqual(steps, 3)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_board_shows_legend(self, mock_stdout):
        """It should display board with legend.

        Args:
            mock_stdout: Mock for stdout to capture print output
        """
        # Arrange: Set default checkers
        self.cli.game.set_default_checkers()

        # Act: Display board
        self.cli.display_board()

        # Assert: Check board elements are present
        output = mock_stdout.getvalue()
        self.assertIn("BACKGAMMON BOARD", output)
        self.assertIn("Legend:", output)
        self.assertIn("○ = Black", output)
        self.assertIn("● = White", output)
        self.assertIn("BEaten:", output)
        self.assertIn("WHouse:", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_board_hidden_counters(self, mock_stdout):
        """It should show hidden counters (xN) when >5 fichas en un punto."""
        # Arrange: preparar más de 5 fichas en dos puntos
        from core.checker import Checker

        board = self.cli.game.__board__
        # Top row point 13 (Black) -> trigger hidden on top loop
        for i in range(7):
            board.add_checker_to_field("13", Checker(100 + i, "Black"))
        # Bottom row point 6 (White) -> trigger hidden on bottom loop
        for i in range(7):
            board.add_checker_to_field("6", Checker(200 + i, "White"))

        # Act
        self.cli.display_board()

        # Assert
        output = mock_stdout.getvalue()
        self.assertIn("x", output)


if __name__ == "__main__":
    unittest.main()
