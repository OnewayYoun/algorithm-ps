import random
from typing import List, Tuple
from collections import defaultdict


def generate_ladder(columns: int) -> List[Tuple[int, int]]:
    bridges = columns * 2
    choices = [i for i in range(1, columns + 1)]
    ladder = []
    for _ in range(bridges):
        choice = random.choice(choices)
        if choice + 1 <= columns:
            ladder.append((choice, choice + 1))
        else:
            ladder.append((choice, choice - 1))
    return ladder


def simulate_ladder(ladder: List[Tuple[int, int]], columns: int) -> defaultdict[int]:
    result = defaultdict(int)
    for column in range(1, columns + 1):
        current = column
        for bridge in ladder:
            if current not in bridge:
                continue
            if current == bridge[0]:
                current = bridge[1]
            else:
                current = bridge[0]
        result[column] = current
    return result


def print_ladder(ladder: List[Tuple[int, int]], columns: int):
    result = [['|'] * columns for _ in range(len(ladder))]
    for idx, bridge in enumerate(ladder):
        result[idx].insert(sorted(bridge)[0], '_')
        for i in range(len(result[idx])-1):
            if result[idx][i] == result[idx][i+1]:
                result[idx][i] = '| '
    for i in result:
        print(''.join(i))


if __name__ == '__main__':
    columns = 10
    ladder = generate_ladder(columns=columns)
    print(ladder)
    print_ladder(ladder, columns)
    result = simulate_ladder(ladder=ladder, columns=columns)
    print(result)
    find = lambda x: result[x]
    print(find(2))
