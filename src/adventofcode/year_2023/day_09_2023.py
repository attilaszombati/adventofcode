from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


def recursive_difference_left(numbers: list[int], can_extrapolate=True):
    if len(numbers) == 1 and numbers[0] != 0:
        can_extrapolate = False
        return numbers, can_extrapolate
    elif all(num == 0 for num in numbers):
        new_value = [0]
        return new_value + numbers, can_extrapolate

    arr = []
    for i, j in zip(numbers[1:], numbers):
        arr.append(i - j)

    next_arr, can_extrapolate = recursive_difference_left(arr, can_extrapolate)
    if not can_extrapolate:
        return next_arr, can_extrapolate

    if len(next_arr) == len(numbers):
        new_value = [numbers[0] - next_arr[0]]
        return new_value + numbers, can_extrapolate
    return recursive_difference_left(arr, can_extrapolate)


def recursive_difference_right(numbers: list[int], can_extrapolate=True):
    if len(numbers) == 1 and numbers[0] != 0:
        can_extrapolate = False
        return numbers, can_extrapolate
    elif all(num == 0 for num in numbers):
        new_value = [0]
        return numbers + new_value, can_extrapolate

    arr = []
    for i, j in zip(numbers[1:], numbers):
        arr.append(i - j)

    next_arr, can_extrapolate = recursive_difference_right(arr, can_extrapolate)
    if not can_extrapolate:
        return next_arr, can_extrapolate

    if len(next_arr) == len(numbers):
        new_value = [numbers[-1] + next_arr[0]]
        return new_value + numbers, can_extrapolate
    return recursive_difference_right(arr, can_extrapolate)


@register_solution(2023, 9, 1)
def part_one(input_data: list[str]):
    res = 0
    for line in input_data:
        line = [int(num) for num in line.split()]
        x, can_extrapolate = recursive_difference_right(line)
        if can_extrapolate:
            res += x[0]

    answer = res

    return answer


@register_solution(2023, 9, 2)
def part_two(input_data: list[str]):
    res = 0
    for line in input_data:
        line = [int(num) for num in line.split()]
        x, can_extrapolate = recursive_difference_left(line)
        if can_extrapolate:
            res += x[0]

    answer = res

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 9)
    part_one(data)
    part_two(data)
