from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


def recursive_difference(numbers: list[int], can_extrapolate=True, part_two=False):
    if len(numbers) == 1 and numbers[0] != 0:
        can_extrapolate = False
        return numbers, can_extrapolate

    elif all(num == 0 for num in numbers):
        if part_two:
            return [0] + numbers, can_extrapolate
        return numbers + [0], can_extrapolate

    arr = [i - j for i, j in zip(numbers[1:], numbers)]
    next_arr, can_extrapolate = recursive_difference(arr, can_extrapolate, part_two=part_two)
    if not can_extrapolate:
        return next_arr, can_extrapolate

    new_value = [numbers[0] - next_arr[0]] if part_two else [numbers[-1] + next_arr[-1]]
    if part_two:
        return new_value + numbers, can_extrapolate
    return numbers + new_value, can_extrapolate


@register_solution(2023, 9, 1)
def part_one(input_data: list[str]):
    res = 0
    for line in input_data:
        line = [int(num) for num in line.split()]
        new_line, can_extrapolate = recursive_difference(line, part_two=False)
        if can_extrapolate:
            res += new_line[-1]

    return res


@register_solution(2023, 9, 2)
def part_two(input_data: list[str]):
    res = 0
    for line in input_data:
        line = [int(num) for num in line.split()]
        new_line, can_extrapolate = recursive_difference(line, part_two=True)
        if can_extrapolate:
            res += new_line[0]

    return res


if __name__ == '__main__':
    data = get_input_for_day(2023, 9)
    part_one(data)
    part_two(data)
