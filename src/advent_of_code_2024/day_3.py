from pathlib import Path
import re

PUZZLE_INPUT = Path('./puzzles/day_3_puzzle.txt').read_text()

MUL_REGEX = re.compile(r"mul\((\d{1,3}).(\d{1,3})\)")
INSTR_REGEX = re.compile(r"mul\((\d{1,3}).(\d{1,3})\)|(do\(\))|(don\'t\(\))")

def solve_first_part(task_input):
    puzzle = ''.join(task_input.splitlines())
    values = MUL_REGEX.findall(puzzle)
    return sum([int(val[0])*int(val[1]) for val in values])

def solve_second_part(task_input):
    puzzle = ''.join(["do()",*task_input.splitlines()])
    enabled = 0
    total = 0
    for a,b,enable,disable in INSTR_REGEX.findall(puzzle):
        if enable or disable:
            enabled = bool(enable)
            continue
        total += int(a)*int(b)*int(enabled)
    return total
if __name__ == "__main__":
    print(solve_first_part(PUZZLE_INPUT))
    print(solve_second_part(PUZZLE_INPUT))
