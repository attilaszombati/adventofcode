from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2021, 21, 1)
def part_one(input_data: list[str]):
    for line in input_data:
        print(line)



@register_solution(2021, 21, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2021, 21, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 21)
    part_one(data)
    # part_two(data)
