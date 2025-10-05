# Automated Reports

## Coverage Report
```text
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
core/board.py        11      0   100%
core/checker.py       8      0   100%
core/dice.py         10      0   100%
core/player.py       12      0   100%
-----------------------------------------------
TOTAL                41      0   100%

```

## Pylint Report
```text
************* Module tests.test_board
tests/test_board.py:1:0: R0801: Similar lines in 2 files
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
            # Places where the checkers have to be put in order to win
            "BHouse": [],
            "WHouse": [],
            # Places where the checkers are put in case they are eaten by another
            "BEaten": [], (duplicate-code)
tests/test_board.py:1:0: R0801: Similar lines in 2 files
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
            # Places where the checkers have to be put in order to win
            "BHouse": [],
            "WHouse": [],
            # Places where the checkers are put in case they are eaten by another
            "BEaten": [], (duplicate-code)

-----------------------------------
Your code has been rated at 9.94/10


```
