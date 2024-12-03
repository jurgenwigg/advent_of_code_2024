from advent_of_code_2024.day_2 import solve_first_part, solve_second_part

_PUZZLE_EXAMPLE_INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
_EXPECTED_FIRST_PART_RESULT = 2
_EXPECTED_SECOND_PART_RESULT = 4

def test_solve_first_part():
    assert solve_first_part(_PUZZLE_EXAMPLE_INPUT.splitlines())[0] == _EXPECTED_FIRST_PART_RESULT

def test_solve_second_part():
    assert solve_second_part(_PUZZLE_EXAMPLE_INPUT.splitlines()) == _EXPECTED_SECOND_PART_RESULT
