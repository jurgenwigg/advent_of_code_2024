from pathlib import Path

PUZZLE_INPUT = Path('./puzzles/day_5_puzzle.txt').read_text()
def split_to_correct_and_incorrect(task_input):
    rules, updates = task_input.split('\n\n')
    rules = list(map(lambda line: line.split('|'), rules.splitlines()))
    updates = list(map(lambda line: line.split(','), updates.splitlines()))
    valid_updates = []
    invalid_updates = []
    for update in updates:
        applicable_rules = []
        valid_update = True
        for index, page in enumerate(update):
            # if not index:
            #     applicable_rules = [rule for rule in rules if rule[0] == page]
            #     applicable_rules = [rule for rule in applicable_rules if rule[-1] in # update]
            # else:
            #     applicable_rules = [rule for rule in rules if page in rule]
            #     applicable_rules = [rule for rule in applicable_rules if rule[-1] in update]
            #applicable_rules = [rule for rule in rules if page in rule]
            #applicable_rules = [rule for rule in applicable_rules if rule[-1] in update]
            applicable_rules = [rule for rule in rules if rule[0] in update and rule[-1] in update]
            for rule in applicable_rules:
                if update.index(rule[0]) > update.index(rule[-1]):
                    valid_update = False
                    break
            if not valid_update:
                continue
        if valid_update:
            valid_updates.append(update)
        else:
            invalid_updates.append([update, applicable_rules])

    return valid_updates, invalid_updates

def fix_incorrect(incorrect_updates):
    fixed_updates = []
    for update, applicable_rules in incorrect_updates:
        for index, page in enumerate(update):
            for rule in applicable_rules:
                if update.index(rule[0]) > update.index(rule[-1]):
                    update[update.index(rule[0])] = rule[-1]
                    update[update.index(rule[-1])] = rule[0]
        fixed_updates.append([update, applicable_rules])
    return fixed_updates

def solve_first_part(task_input):
    valid_updates, _ = split_to_correct_and_incorrect(task_input)
    result = sum([int(update[(len(update)-1)//2]) for update in valid_updates])
    return result

def solve_second_part(task_input):
    _, invalid_updates = split_to_correct_and_incorrect(task_input)
    fixed_updates = fix_incorrect(invalid_updates)
    fixed_updates = fix_incorrect(fixed_updates)
    result = sum([int(update[(len(update)-1)//2]) for update, _ in fixed_updates])
    return result

if __name__ == "__main__":
    print(solve_first_part(PUZZLE_INPUT))
    print(solve_second_part(PUZZLE_INPUT))
