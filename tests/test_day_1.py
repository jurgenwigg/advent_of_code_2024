from advent_of_code_2024.day_1 import solve_first_task, solve_second_task

_FIRST_PUZZLE = """3   4
4   3
2   5
1   3
3   9
3   3
"""
_SECOND_PUZZLE = _FIRST_PUZZLE
_EXPECTED_FIRST_PUZZLE_RESULT = 11
_EXPECTED_SECOND_PUZZLE_RESULT = 31

def test_solve_first_task():
    assert solve_first_task(_FIRST_PUZZLE) == _EXPECTED_FIRST_PUZZLE_RESULT

def test_solve_second_task():
    assert solve_second_task(_SECOND_PUZZLE) == _EXPECTED_SECOND_PUZZLE_RESULT
