from collections import defaultdict, deque

import math

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2023, 8, 1)
def part_one(parents: dict):
    counter = 0
    target = "AAA"

    while target != "ZZZ":
        inst = instructions[0]
        instructions.rotate(-1)

        counter += 1
        next_start = parents[target][0][0] if inst == "L" else parents[target][0][1]
        target = next_start

    return counter


@register_solution(2023, 8, 2)
def part_two(parents: dict):
    start_elems = deque(i for i in parents if i.endswith("A"))
    counter = 0

    hm = {}
    for start in start_elems:

        s = start
        while not s.endswith("Z"):
            inst = instructions.popleft()
            instructions.append(inst)

            counter += 1
            next_start = parents[s][0][0] if inst == "L" else parents[s][0][1]
            s = next_start

        hm[start] = counter
        counter = 0

    answer = math.lcm(*hm.values())

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 8)

    instructions = deque(data[0])
    map_system = [i.split(" = ") for i in data[1:] if i]
    parents = defaultdict(list)
    for elem in map_system:
        next_steps = elem[1][1:-1].split(", ")
        parent, child = elem[0], (next_steps[0], next_steps[1])
        parents[parent].append(child)

    part_one(parents)
    part_two(parents)
