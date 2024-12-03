from contextlib import ContextDecorator
from pathlib import Path
from collections import OrderedDict

PUZZLE_INPUT = Path('./puzzles/day_2_puzzle.txt').read_text().splitlines()

def solve_first_part(task_input):
    safe_levels = 0
    unsafe_levels = []
    for levels in task_input:
        level = [int(elem) for elem in levels.split()]
        is_decreasing = level == sorted(level, reverse=True)
        is_increasing = level == sorted(level, reverse=False)
        if not any([is_decreasing, is_increasing]):
            unsafe_levels.append(level)
            continue
        levels_diff = []
        for index, elem in enumerate(level[:-1]):
            levels_diff.append(1<=abs(elem-level[index+1])<=3)
        if all(levels_diff):
            safe_levels+=1
        else:
            unsafe_levels.append(level)
    result = safe_levels, unsafe_levels
    return result

def extrema(a, n):

    count = 0
    # start loop from
    # position 1 till n-1
    for i in range(1, n - 1) :
        # only one condition
        # will be true
        # at a time either
        # a[i] will be greater
        # than neighbours or
        # less than neighbours

        # check if a[i] if
        # greater than both its
        # neighbours, then add
        # 1 to x
        count += (a[i] > a[i - 1] and a[i] > a[i + 1]);

        # check if a[i] if
        # less than both its
        # neighbours, then
        # add 1 to x
        count += (a[i] < a[i - 1] and a[i] < a[i + 1]);

    return count


def remove_duplicates(level):
    new_level = []
    no_of_duplicates = 0
    removed_once = False
    for elem in level:
        if elem not in new_level:
            new_level.append(elem)
            continue
        if removed_once:
            return False
        no_of_duplicates += 1
    return new_level, no_of_duplicates

def solve_second_part(task_input):
    safe_levels, levels = solve_first_part(task_input=task_input)

    debug=[]
    for level in levels:
        check = [elem for index, elem in enumerate(level[:-1]) if abs(elem-level[index+1])>3]
        if bool(check):
            continue
        check = remove_duplicates(level)
        if not check:
            continue
        else:
            level = check[0]

        check = extrema(level, len(level))
        print(f"{level=} | {check=}")
        if not check or check==1:
            dec = intersection(level, sorted(level, reverse=True))
            inc = intersection(level, sorted(level, reverse=False))
            is_decreasing = level == sorted(level, reverse=True)
            is_increasing = level == sorted(level, reverse=False)

            if not any([is_decreasing, is_increasing]):
                continue
            safe_levels+=1
    print(f"{debug=}")
    result=len(debug)
    return safe_levels

def second_try(data):
    def is_safe(row):
        inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
            return True
        return False

    safe_count = sum([is_safe(row) for row in data])
    print(safe_count)

    safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])
    print(safe_count)

if __name__ == "__main__":
    # print(solve_first_part(PUZZLE_INPUT)[0])
    # print(solve_second_part(PUZZLE_INPUT))
    second_try(data = [[int(y) for y in x.split(' ')] for x in Path('./puzzles/day_2_puzzle.txt').read_text().splitlines()])
