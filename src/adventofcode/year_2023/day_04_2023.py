from collections import defaultdict

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2023, 4, 1)
def part_one(input_data: list[str]):

    sum_line = 0
    parents = defaultdict(list)

    def recursive_find(parents, children):

        sub_children = 0

        if not children:
            return 0

        for child in children:
            if child in parents:
                sub_children += 1 + recursive_find(parents, parents[child])

        return sub_children

    for line in input_data:
        card_number = line.split(":")[0][-3:].strip()
        line = line.split(":")[1].strip()
        winning_numbers = line.split(" | ")[0].split(" ")
        my_numbers = line.split(" | ")[1].split(" ")

        for winner in winning_numbers:
            if winner == "":
                continue
            if winner in my_numbers:
                sum_line += 1

        parents[int(card_number)] = list(i for i in range(int(card_number) + 1, sum_line + int(card_number) + 1))
        sum_line = 0

    answer = sum(1 + recursive_find(parents, parents[parent]) for parent in parents)
    return answer


@register_solution(2023, 4, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2023, 4, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 4)
    part_one(data)
    part_two(data)
