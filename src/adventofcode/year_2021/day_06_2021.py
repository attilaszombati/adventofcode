from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day

from collections import defaultdict, deque


@register_solution(2021, 6, 1)
def part_one(input_data: list[str]):

    print(input_data)
    input_data = [int(x) for x in input_data[0].split(",")]

    def count_fish(days, fish):

        queue = deque([0 for _ in range(9)])
        for f in fish:
            queue[f] += 1

        for day in range(days):
            print(f"Day {day}: {queue}")
            queue[7] += queue[0]
            queue.rotate(-1)

        return sum(queue)

    return count_fish(80, input_data)

    # [3, 4, 3, 1, 2] --> deque([0, 1, 1, 2, 1, 0, 0, 0, 0])
    # [2, 3, 2, 0, 1] --> deque([1, 1, 2, 1, 0, 0, 0, 0, 8])






@register_solution(2021, 6, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2021, 6, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 6)
    part_one(data)
    # part_two(data)
