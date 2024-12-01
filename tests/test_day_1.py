from advent_of_code_2024.day_1 import solve_first_part, solve_second_part

_PUZZLE_EXAMPLE_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3
"""
_EXPECTED_FIRST_PART_RESULT = 11
_EXPECTED_SECOND_PART_RESULT = 31

def test_solve_first_part():
    assert solve_first_part(_PUZZLE_EXAMPLE_INPUT) == _EXPECTED_FIRST_PART_RESULT

def test_solve_second_part():
    assert solve_second_part(_PUZZLE_EXAMPLE_INPUT) == _EXPECTED_SECOND_PART_RESULT
