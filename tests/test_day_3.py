from advent_of_code_2024.day_3 import solve_first_part, solve_second_part

_PUZZLE_FIRST_PART_EXAMPLE_INPUT = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
_PUZZLE_SECOND_PART_EXAMPLE_INPUT ="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))don't()_mul(5,5)XXX+mul(32,64](mul(11,8)un"
_EXPECTED_FIRST_PART_RESULT = 161
_EXPECTED_SECOND_PART_RESULT = 48

def test_solve_first_part():
    assert solve_first_part(_PUZZLE_FIRST_PART_EXAMPLE_INPUT) == _EXPECTED_FIRST_PART_RESULT

def test_solve_second_part():
    assert solve_second_part(_PUZZLE_SECOND_PART_EXAMPLE_INPUT) == _EXPECTED_SECOND_PART_RESULT
