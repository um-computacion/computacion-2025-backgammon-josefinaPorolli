# Automated Reports

## Coverage Report
```text
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
cli/__init__.py               0      0   100%
core/backgammon_game.py     262      5    98%   77, 266, 332, 479-480
core/board.py                11      0   100%
core/checker.py               8      0   100%
core/dice.py                 10      0   100%
core/player.py               12      0   100%
-------------------------------------------------------
TOTAL                       303      5    98%

```

## Pylint Report
```text
************* Module core.backgammon_game
core/backgammon_game.py:295:0: C0301: Line too long (109/100) (line-too-long)
core/backgammon_game.py:300:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:366:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:464:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:474:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:481:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:485:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:11:0: R0902: Too many instance attributes (36/7) (too-many-instance-attributes)
core/backgammon_game.py:404:12: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game.py:431:12: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game.py:466:11: R1714: Consider merging these comparisons with 'in' by using 'origin in ('BEaten', 'WEaten')'. Use a set instead if elements are hashable. (consider-using-in)
************* Module tests.test_backgammon_game
tests/test_backgammon_game.py:394:0: C0301: Line too long (102/100) (line-too-long)
tests/test_backgammon_game.py:395:0: C0301: Line too long (102/100) (line-too-long)
tests/test_backgammon_game.py:396:0: C0301: Line too long (101/100) (line-too-long)
tests/test_backgammon_game.py:397:0: C0301: Line too long (101/100) (line-too-long)
tests/test_backgammon_game.py:402:0: C0301: Line too long (102/100) (line-too-long)
tests/test_backgammon_game.py:404:0: C0301: Line too long (125/100) (line-too-long)
tests/test_backgammon_game.py:407:0: C0301: Line too long (102/100) (line-too-long)
tests/test_backgammon_game.py:408:0: C0301: Line too long (102/100) (line-too-long)
tests/test_backgammon_game.py:409:0: C0301: Line too long (106/100) (line-too-long)
tests/test_backgammon_game.py:417:0: C0301: Line too long (101/100) (line-too-long)
tests/test_backgammon_game.py:419:0: C0301: Line too long (124/100) (line-too-long)
tests/test_backgammon_game.py:422:0: C0301: Line too long (101/100) (line-too-long)
tests/test_backgammon_game.py:423:0: C0301: Line too long (101/100) (line-too-long)
tests/test_backgammon_game.py:424:0: C0301: Line too long (106/100) (line-too-long)
tests/test_backgammon_game.py:431:0: C0301: Line too long (130/100) (line-too-long)
tests/test_backgammon_game.py:433:0: C0301: Line too long (106/100) (line-too-long)
tests/test_backgammon_game.py:434:0: C0301: Line too long (102/100) (line-too-long)
tests/test_backgammon_game.py:443:0: C0301: Line too long (102/100) (line-too-long)
tests/test_backgammon_game.py:444:0: C0301: Line too long (106/100) (line-too-long)
tests/test_backgammon_game.py:445:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_backgammon_game.py:474:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_backgammon_game.py:294:4: R0915: Too many statements (56/50) (too-many-statements)
tests/test_backgammon_game.py:5:0: R0904: Too many public methods (21/20) (too-many-public-methods)
************* Module tests.test_checker
tests/test_checker.py:1:0: R0801: Similar lines in 2 files
==core.board:[14:42]
==tests.test_board:[19:45]
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": [],
        "10": [],
        "11": [],
        "12": [],
        "13": [],
        "14": [],
        "15": [],
        "16": [],
        "17": [],
        "18": [],
        "19": [],
        "20": [],
        "21": [],
        "22": [],
        "23": [],
        "24": [],
        "BHouse": [],
        "WHouse": [],
        "BEaten": [], (duplicate-code)
tests/test_checker.py:1:0: R0801: Similar lines in 2 files
==core.board:[19:42]
==tests.test_board:[86:107]
        "7": [],
        "8": [],
        "9": [],
        "10": [],
        "11": [],
        "12": [],
        "13": [],
        "14": [],
        "15": [],
        "16": [],
        "17": [],
        "18": [],
        "19": [],
        "20": [],
        "21": [],
        "22": [],
        "23": [],
        "24": [],
        "BHouse": [],
        "WHouse": [],
        "BEaten": [], (duplicate-code)

-----------------------------------
Your code has been rated at 9.50/10


```
