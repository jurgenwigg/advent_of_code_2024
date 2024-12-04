from advent_of_code_2024.day_4 import solve_first_part, solve_second_part

_PUZZLE_EXAMPLE_INPUT = """
test content
"""
_EXPECTED_FIRST_PART_RESULT = -1
_EXPECTED_SECOND_PART_RESULT = -1

def test_solve_first_part():
    assert solve_first_part(_PUZZLE_EXAMPLE_INPUT) == _EXPECTED_FIRST_PART_RESULT

def test_solve_second_part():
    assert solve_second_part(_PUZZLE_EXAMPLE_INPUT) == _EXPECTED_SECOND_PART_RESULT
