import re
import regex

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day

digit_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def replace_string_to_digits_from_start(line: str) -> str:
    regex_pattern = r"\d|one|two|three|four|five|six|seven|eight|nine"
    digits = regex.findall(regex_pattern, line, overlapped=True)
    mapped = [digit_dict.get(x, x) for x in digits]
    return mapped[0] + mapped[-1]


@register_solution(2023, 1, 1)
def part_one(input_data: list[str]):
    summary = 0
    for line in input_data:
        first_digit = re.search(r"\d", line)
        reversed_line = line[::-1]
        last_digit = re.search(r"\d", reversed_line)
        s = f"{line[first_digit.start()]}{reversed_line[last_digit.start()]}"
        summary += int(s)
    answer = summary

    if not answer:
        raise SolutionNotFoundException(2023, 1, 1)

    return answer


@register_solution(2023, 1, 2)
def part_two(input_data: list[str]):
    summary = 0
    for line in input_data:
        line = replace_string_to_digits_from_start(line)
        first_digit = re.search(r"\d", line)
        reversed_line = line[::-1]
        last_digit = re.search(r"\d", reversed_line)
        s = f"{line[first_digit.start()]}{reversed_line[last_digit.start()]}"
        summary += int(s)
    answer = summary

    if not answer:
        raise SolutionNotFoundException(2023, 1, 1)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 1)
    part_one(data)
    part_two(data)
