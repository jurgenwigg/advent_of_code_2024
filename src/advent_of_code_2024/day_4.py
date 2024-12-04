from pathlib import Path

PUZZLE_INPUT = Path('./puzzles/day_4_puzzle.txt').read_text()

def _text_in_row(puzzle):
    result = 0
    for line in puzzle:
        for index, _ in enumerate(line):
            window = ''.join(line[index:index+4])
            if len(window) < 4:
                continue
            result += int(bool(window == "XMAS" or window=="SAMX"))
    return result

def _text_diagonal_right(puzzle):
    result = 0
    for line_index, line in enumerate(puzzle[:-3]):
        for char_index, _ in enumerate(line[:-3]):
            a=puzzle[line_index][char_index]
            b=puzzle[line_index+1][char_index+1]
            c=puzzle[line_index+2][char_index+2]
            d=puzzle[line_index+3][char_index+3]

            window = ''.join([a,b,c,d])
            result += int(bool(window == "XMAS" or window=="SAMX"))
    return result

def _text_diagonal_left(puzzle):
    result = 0
    for line_index, line in enumerate(puzzle[:-3]):
        for char_index, _ in enumerate(line[:-3]):
            a=puzzle[line_index][char_index+3]
            b=puzzle[line_index+1][char_index+2]
            c=puzzle[line_index+2][char_index+1]
            d=puzzle[line_index+3][char_index]

            window = ''.join([a,b,c,d])
            print(f'{window=} | {int(bool(window == "XMAS" or window=="SAMX"))=}')
            result += int(bool(window == "XMAS" or window=="SAMX"))
    return result

def _text_vertical(puzzle):
    result = 0
    puzzle = list(map(list, zip(*puzzle)))
    for line in puzzle:
        for index, _ in enumerate(line):
            window = ''.join(line[index:index+4])
            if len(window) < 4:
                continue
            result += int(bool(window == "XMAS" or window=="SAMX"))
    return result

def solve_first_part(task_input):
    puzzle = task_input.splitlines()
    line_len = len(puzzle)
    result = 0
    result += _text_in_row(puzzle)
    result += _text_diagonal_right(puzzle)
    result += _text_diagonal_left(puzzle)
    result += _text_vertical(puzzle)
    return result

def solve_second_part(task_input):
    result = -1
    return result

if __name__ == "__main__":
    print(solve_first_part(PUZZLE_INPUT))
    print(solve_second_part(PUZZLE_INPUT))
