from advent_of_code_2024.day_5 import solve_first_part, solve_second_part

_PUZZLE_EXAMPLE_INPUT = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
_EXPECTED_FIRST_PART_RESULT = 143
_EXPECTED_SECOND_PART_RESULT = 123

def test_solve_first_part():
    assert solve_first_part(_PUZZLE_EXAMPLE_INPUT) == _EXPECTED_FIRST_PART_RESULT

def test_solve_second_part():
    assert solve_second_part(_PUZZLE_EXAMPLE_INPUT) == _EXPECTED_SECOND_PART_RESULT
