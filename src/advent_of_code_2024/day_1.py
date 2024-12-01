from pathlib import Path

FIRST_PUZZLE_INPUT = Path('./puzzles/day_1_first_puzzle.txt').read_text()
SECOND_PUZZLE_INPUT = FIRST_PUZZLE_INPUT

def solve_first_task(task_input):
    left = []
    right = []
    result = 0
    for line in task_input.splitlines():
        if not line:
            continue
        left_val, right_val = line.strip().split()
        left.append(int(left_val.strip()))
        right.append(int(right_val.strip()))

    left = sorted(left)
    right = sorted(right)

    for index,value in enumerate(left):
        result+=abs(right[index]-value)

    return result

def solve_second_task(task_input):
    left = []
    right = []
    result = 0
    for line in task_input.splitlines():
        if not line:
            continue
        left_val, right_val = line.strip().split()
        left.append(int(left_val.strip()))
        right.append(int(right_val.strip()))

    for value in left:
        result+=value*right.count(value)
    return result

if __name__ == "__main__":
    print(solve_first_task(FIRST_PUZZLE_INPUT))
    print(solve_second_task(SECOND_PUZZLE_INPUT))
