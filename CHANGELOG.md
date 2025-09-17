# BACKGAMMON - CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.17] - 17/09/25

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