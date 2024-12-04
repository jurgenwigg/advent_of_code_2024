from advent_of_code_2024.day_4 import solve_first_part, solve_second_part

_PUZZLE_EXAMPLE_INPUT = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
"""
_SECOND_PUZZLE_EXAMPLE_INPUT = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""
_EXPECTED_FIRST_PART_RESULT = 18
_EXPECTED_SECOND_PART_RESULT = 9

def test_solve_first_part():
    assert solve_first_part(_PUZZLE_EXAMPLE_INPUT) == _EXPECTED_FIRST_PART_RESULT

def test_solve_second_part():
    assert solve_second_part(_SECOND_PUZZLE_EXAMPLE_INPUT) == _EXPECTED_SECOND_PART_RESULT
