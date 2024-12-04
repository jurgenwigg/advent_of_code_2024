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
_EXPECTED_FIRST_PART_RESULT = 18
_EXPECTED_SECOND_PART_RESULT = -1

def test_solve_first_part():
    assert solve_first_part(_PUZZLE_EXAMPLE_INPUT) == _EXPECTED_FIRST_PART_RESULT

def test_solve_second_part():
    assert solve_second_part(_PUZZLE_EXAMPLE_INPUT) == _EXPECTED_SECOND_PART_RESULT
