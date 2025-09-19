# Automated Reports

## Coverage Report
```text
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
core/checker.py       8      0   100%
core/dice.py         10      0   100%
core/player.py       12      0   100%
-----------------------------------------------
TOTAL                30      0   100%

```

## Pylint Report
```text
************* Module core.backgammon_game
core/backgammon_game.py:24:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:32:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:39:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:41:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:61:0: C0301: Line too long (101/100) (line-too-long)
core/backgammon_game.py:66:0: C0301: Line too long (101/100) (line-too-long)
core/backgammon_game.py:69:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:83:0: C0301: Line too long (108/100) (line-too-long)
core/backgammon_game.py:84:0: C0301: Line too long (105/100) (line-too-long)
core/backgammon_game.py:94:0: C0301: Line too long (109/100) (line-too-long)
core/backgammon_game.py:105:0: C0301: Line too long (102/100) (line-too-long)
core/backgammon_game.py:106:0: C0301: Line too long (101/100) (line-too-long)
core/backgammon_game.py:110:0: C0301: Line too long (141/100) (line-too-long)
core/backgammon_game.py:111:0: C0301: Line too long (146/100) (line-too-long)
core/backgammon_game.py:112:0: C0301: Line too long (110/100) (line-too-long)
core/backgammon_game.py:114:0: C0301: Line too long (124/100) (line-too-long)
core/backgammon_game.py:120:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:128:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:134:0: C0301: Line too long (109/100) (line-too-long)
core/backgammon_game.py:145:0: C0301: Line too long (101/100) (line-too-long)
core/backgammon_game.py:150:0: C0301: Line too long (140/100) (line-too-long)
core/backgammon_game.py:151:0: C0301: Line too long (143/100) (line-too-long)
core/backgammon_game.py:152:0: C0301: Line too long (110/100) (line-too-long)
core/backgammon_game.py:154:0: C0301: Line too long (118/100) (line-too-long)
core/backgammon_game.py:160:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:168:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:170:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:180:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammon_game.py:3:0: E0401: Unable to import 'board' (import-error)
core/backgammon_game.py:4:0: E0401: Unable to import 'player' (import-error)
core/backgammon_game.py:5:0: E0401: Unable to import 'dice' (import-error)
core/backgammon_game.py:6:0: E0401: Unable to import 'checker' (import-error)
core/backgammon_game.py:47:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
core/backgammon_game.py:45:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
core/backgammon_game.py:59:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
core/backgammon_game.py:56:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
core/backgammon_game.py:72:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
core/backgammon_game.py:70:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
core/backgammon_game.py:88:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
core/backgammon_game.py:98:24: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game.py:102:28: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game.py:107:36: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game.py:114:52: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game.py:88:8: R1702: Too many nested blocks (12/5) (too-many-nested-blocks)
core/backgammon_game.py:138:24: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game.py:142:28: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game.py:147:36: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game.py:154:52: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/backgammon_game.py:129:8: R1702: Too many nested blocks (12/5) (too-many-nested-blocks)
core/backgammon_game.py:86:4: R0911: Too many return statements (18/6) (too-many-return-statements)
core/backgammon_game.py:86:4: R0912: Too many branches (36/12) (too-many-branches)
core/backgammon_game.py:86:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
core/backgammon_game.py:6:0: W0611: Unused Checker imported from checker (unused-import)
************* Module tests.test_checker
tests/test_checker.py:6:0: C0115: Missing class docstring (missing-class-docstring)

-----------------------------------
Your code has been rated at 6.15/10


```
