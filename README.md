# Backgammon (Final project)

Author: Josefina Porolli Serpa (Legajo: 64133)
Course: Computación I — 2025

## Basic project structure

- `core/` - Game core logic (board, checkers, dice, player, game logic).
- `cli/` - Command-line interface implementation and entry point.
- `pygame_ui/` - Pygame graphical interface (main window, rendering, input handling).
- `tests/` - Unit tests for core components.
- `requirements.txt` - Python dependencies (install with pip).
- `README.md` - This file.
- `JUSTIFICACION.md` - Helpful file for presenting this project.
- `CHANGELOG.md` - Document describing thee different changes made to the project.

## Requirements

- Python 3.8+ (any modern 3.x should work)
- Install dependencies listed in `requirements.txt`:
```
python -m pip install -r requirements.txt
```

## Run the CLI interface

Start the text-based interface from the project root:

```
python -m cli.cli
```

## Run the Pygame graphical interface

Start the graphical UI (the main window is `pygame_ui/game_interface.py`):

```
python -m pygame_ui.game_interface
```

The game window size is defined by `WIDTH` and `HEIGHT` constants in `pygame_ui/game_interface.py`.

## Tests and coverage

Run the unit tests with the standard library `unittest` runner:

```
python -m unittest discover -v
```

Run a single test module (example with tests for board module):

```
python -m unittest tests.test_board
```

Generate coverage report:

```
python -m coverage run -m unittest discover; python -m coverage report
```

## Controls (graphical UI)

- Name input: enter names for BLACK and WHITE at startup.
- First turn: an automatic dice roll determines who starts; press any key to continue.
- Roll dice: click the `ROLL DICE` button in the right control panel for the active player.
- Select a checker: click the point (triangle) or the `EATEN` area (if you have eaten checkers) to choose the origin.
- Choose a dice: after selecting a point, click the representation of a dice on the right panel to apply that move.
- Used dice: dice already used are visually grayed-out and cannot be selected.
- Skip turn: if no valid moves are available, the `SKIP TURN` button appears and can be used to pass.
- Messages: game messages appear in the middle-right message area and describe required actions or errors.

## Game flow

1. Enter player names.
2. The game determines who starts by rolling dice for both players.
3. Active player clicks `ROLL DICE` to obtain moves.
4. Player selects a point (or `EATEN` area) with their checker, then clicks a dice to move.
5. Each dice usage reduces available moves; doubles give four moves.
6. When a player has no valid moves, they can skip their turn.
7. The game ends when one player bears off all their checkers; the winner's name is shown and further rolls are disabled.

## Notes

- If UI elements appear misaligned, check `pygame_ui/game_interface.py` for the layout constants (margins, control panel sizes).
- For development, you can run individual modules directly from the project root using the `-m` flag.
- Report bugs or unexpected behavior by opening an issue and including screenshots and the console output.

Enjoy the game!

