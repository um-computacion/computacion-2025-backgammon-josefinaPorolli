# BACKGAMMON - CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.7] - 28/10/25

### Changed

- Modified Backgammon Game in order to fulfill SRP principle. Now the responsibilities of making checkers and checking moves are no longer BackgammonGame's.

## [2.0.6] - 27/10/25

### Added

- Developed README file.

## [2.0.5] - 27/10/25

### Changed

- Pygame: mapped WEaten and BEaten checkers. Changed the green color in the selected checkers. Changed the winner message. The messages of the game are now shown on the player control section.

## [2.0.4] - 25/10/25

### Added

- Pygame: Methods for rolling the dice and moving checkers. Bugs: when a checker is put on bar, the graphics don´t work properly and the checker is not removed from the point, messages would look better in each player's control square, the used dice should be removed from the graphics and don't quite like the green in a selected point.

## [2.0.3] - 22/10/25

### Added

- Pygame: Methods for getting the player's names and using them. Also added a method that creates a new screen to set the first turn based on the value of each dice.

## [2.0.2] - 22/10/25

### Changed

- Pygame: Mapped fields in the board with the triangles in the interface, and the special ones with rectangles. Also added the main game in the code and set the default checkers with its corresponding representation (circles)

## [2.0.1] - 21/10/25

### Changed

- Restarted the cli interface so that I could have everything more controlled. Just made the background and some basic divisions wit AI's help.

## [2.0.0] - 19/10/25

### Added

- Added a primitive AI generated pygame interface as what will be a guide, as I have never in my life used pygame so I need at least something to start with :/

## [1.0.3] - 18/10/25

### Changed

- Finished mechanism in CLI. The validation for when there are absolutely no moves that can be made, is now evaluated after each move and not just after changing turns.

## [1.0.2] - 18/10/25

### Changed

- Upgraded CLI interface. When the first turn is set, it shows the actual player's name. Added validations for when the origin put by the player is not valid.

## [1.0.1] - 18/10/25

### Changed

- Upgraded CLI interface. Fixed the display of the board, changed the colour of the representation of the checkers (now it has to be used in a dark mode console), added validations for invalid inputs of steps.

## [1.0.0] - 13/10/25

### Added

- CLI interface for playing. It is far from working the way it should because I used an AI response as a guide for it.

## [0.1.11] - 11/10/25

### Added

- Finished tests for backgammon game

### Changed

- Changed some details in move_checker, as in some cases it tried to move more than 1 checker.
- Finished tests for backgammon game

## [0.1.10] - 11/10/25

### Added

- Almost finished tests for backgammon game

### Changed

- Changed is valid bear of methods. They only checked if there was a possibility to take a checker to the house, but didn't consider the origin as a parameter. Tests wouldn't pass.
- Changed mechanism in move_checker method in Backgammon Game class, so that we only need the origin and the steps to make a move. Also added a mechanism to eat the opponent's checker if possible, take out an eaten checker and move a checker to the house (destination = house).
- Changed the way that check move to house methods evaluate the origin, as it is not always a number.

### Deleted

- Deleted method move_checker_to_house. Move checker just sets the destination to the house if the move is valid.

## [0.1.9] - 10/10/25

### Changed

- Changed different aspects in tests/ in order to meet pylint expectations

## [0.1.8] - 10/10/25

### Added

- Added method _check_take_out_with_opponent_checker to backgammon game class as a correction to the test and in order to meet pylint expectations

### Changed

- Modifications in type of variable in get_destination_point, check_opponent_checkers and check_take_out_eaten_checker method in class Backgammon Game
- Modified check_eatable_checker. Used get_colour() method because it was just evaulating the list and not the colour of the checker in the field
- Changed the names of the variables of each checker to meet pylint expectations
- Changed the range of points that _is_valid_bear_off method evaluates

## [0.1.7] - 08/10/25

### Added

- Added tests for backgammon game. Set and get turn, set default checkers and check winner. Unittest used places in memory for checking the default checkers, so I had to look for an alternative usind the IDs i gave each checker.

### Changed

- Added __ in variables for test_board.py
- Changed method set_default_cehckers for getting an easier access to the checkers and added each single checker in the constructor.

## [0.1.6] - 07/10/25

### Added

- Added set_default_checkers method to Backgammon Game class for setting the initial position of the checkers at the beginning of the game.

## [0.1.5] - 07/10/25

### Changed

- Justificacion.md created and all the information in README.md was transferred as I mistakenly did that part the other way around.

## [0.1.4] - 29/09/25

### Added

- Test module for methods in class board

## [0.1.3] - 29/09/25

### Changed

- Class Backgammon Game: fixed pylint errors in core/backgammon_game.py related to the method that checks the move. Added sub-methods to reduce the quantity of returns in each method and fixed inconsistent return statements.

## [0.1.2] - 21/09/25

### Changed

- Class Backgammon Game: fixed pylint errors in core/backgammon_game.py related to checking each colour's move to house method. Added sub-methods to reduce the quantity of returns in each method.

## [0.1.1] - 21/09/25

### Changed

- Class Backgammon Game: fixed some general pylint errors in core/ and tests/ directories.

## [0.1.0] - 20/09/25

### Added

- Class Backgammon Game: added method for checking winner. The class now should have all the methods I need. This will be checked with tests and implementation.

## [0.0.22] - 20/09/25

### Added

- Class Backgammon Game: added method for checking if the chosen checker can be moved to the house.

### Changed

- Class Backgammon Game: replaced the block in check_move that checked if the checker could be moved to the house for the new method
- Class Backgammon Game: before moving the checker in move_checker_to_house(), the method checks if the move is valid with the new method.

## [0.0.21] - 20/09/25

### Added

- Class Backgammon Game: added methods for moving checkers.
- Class Backgammon Game: added a method for checking if the player can take out an eaten checker.
- Class Backgammon Game: added a method for getting the destination. Useful for checking if the checker can be moved to the house.
- Class Backgammon Game: added a method for moving the checker to the house.
- Class Board: added two methods: one for adding a checker to a field (also useful for the beginning of the game with the default positions), and another for removing a field from an origin (for moving checkers).

### Changed

- Changed the way the method eat_opponent_checker works with new methods in class Board.
- Changed the logic of check_move in Backgammon Game, as the first thing the game needs to do is to check if the player must take out eaten checkers.

## [0.0.20] - 19/09/25

### Changed

- Class Backgammon Game: added methods for checking valid moves. Fixed general check method implementing all necessary kinds of checks. Also added method for eating the opponent´s checker.

## [0.0.19] - 17/09/25

### Added

- Module for class backgammon game, implementing the methods for turns and checking basic moves so that the checkers don't go off the main board.

## [0.0.18] - 17/09/25

### Changed

- Class board: changed the idea of the class, as the fields in the board have to keep instances of class Checker, not quantity of checkers and their colour.

## [0.0.17] - 17/09/25

### Added

- Module for class board

## [0.0.16] - 11/09/25

### Changed

- Unique id for each element of type Checker

### Removed
- Setter for the colour of the checker, as it is already set when each instance is declared
- Test for colour setter in class Checker

## [0.0.15] - 11/09/25

### Added

- Test module for class checker
- Prompt in promptsAI/prompts-testing.md

### Changed

- Changed wrong dates in CHANGELOG.md file (accidentally put August when actually some commits were done in September)

## [0.0.14] - 11/09/25

### Added

- Module for class Checker

## [0.0.13] - 10/09/25

### Added

- README file with basic structure

## [0.0.12] - 09/09/25

### Added

- __init__.py files in core/ and tests/ because tests were not detecting the imported modules

### Changed

- Details in test/ modules in order to fulfill QA requirements up to now

## [0.0.12] - 09/09/25

### Added

- ./github/workflows/ci.yml for continuous integration

### Changed
- Modules in core/ in order to correct errors marked by pylint

## [0.0.11] - 09/09/25

### Added

- pylint in requirements.txt
- .pylintrc file

## [0.0.10] - 29/08/25

### Added

- Tests for Dice.
- XML and HTML reports with coverage

## [0.0.9] - 29/08/25

### Added

- Class Dice with attributes and methods

## [0.0.8] - 28/08/25

### Added

- File for class Dice (empty file)

## [0.0.7] - 28/08/25

### Added

- .coveragerc file to omit venv and tests folders
- coverage xml with Player class testing
- coverage html with Player class testing

## [0.0.6] - 28/08/25

### Added

- Tests for class Player

## [0.0.5] - 27/08/25

### Added

- Files that clarify every interaction with artificial intelligence for this project

## [0.0.4] - 27/08/25

### Added

- venv and gitignore files

## [0.0.3] - 27/08/25

### Added

- Requirements file for coverage installation

## [0.0.2] - 26/08/25

### Added

- CHANGELOG file

## [0.0.1] - 25/08/25

### Added

- Class Player with attributes name and colour to identify each player itself in human language, and the colour of the checkers they are playing with