from pathlib import Path

PUZZLE_INPUT = Path('./puzzles/day_1_puzzle.txt').read_text()

def _prepare_data(raw_data):
    left = []
    right = []
    for line in raw_data.splitlines():
        if not line:
            continue
        left_val, right_val = line.strip().split()
        left.append(int(left_val.strip()))
        right.append(int(right_val.strip()))
    return left, right

def solve_first_part(task_input):
    left, right = _prepare_data(task_input)
    result = 0

    left = sorted(left)
    right = sorted(right)

    for index,value in enumerate(left):
        result+=abs(right[index]-value)

    return result

def solve_second_part(task_input):
    left, right = _prepare_data(task_input)
    result = 0

    for value in left:
        result+=value*right.count(value)
    return result

if __name__ == "__main__":
    print(solve_first_part(PUZZLE_INPUT))
    print(solve_second_part(PUZZLE_INPUT))
