from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2023, 2, 1)
def part_one(input_data: list[str]):

    sum_games = 0

    for line in input_data:
        split_line = " ".join(line.split(":")[1:]).split(";")

        min_blue = 0
        min_red = 0
        min_green = 0

        for game in split_line:

            for colors in game[1:].split(","):

                if " " == colors[0]:
                    colors = colors[1:]

                if "blue" in colors:
                    blue = int(colors.split(" ")[0])
                    if blue > min_blue:
                        min_blue = blue
                elif "red" in colors:
                    red = int(colors.split(" ")[0])
                    if red > min_red:
                        min_red = red
                elif "green" in colors:
                    green = int(colors.split(" ")[0])
                    if green > min_green:
                        min_green = green

        print(f"Min blue: {min_blue}, Min red: {min_red}, Min green: {min_green}")
        print(f"product of min colors: {min_blue * min_red * min_green}")

        sum_games += min_blue * min_red * min_green

    print(f"Sum of good games: {sum_games}")


@register_solution(2023, 2, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2023, 2, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 2)
    part_one(data)
    part_two(data)
