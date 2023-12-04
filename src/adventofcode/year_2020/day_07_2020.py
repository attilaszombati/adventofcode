from pprint import pprint
from collections import defaultdict, deque

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


def part_one(input_data: list[str]):

    parents = defaultdict(list)
    children = defaultdict(list)

    target = "shiny gold"

    for line in input_data:
        line = line.replace(" bags", "").replace(" bag", "").replace(".", "")
        line = line.split(" contain ")
        parent = line[0]
        for child in line[1].split(", "):
            if child == "no other":
                continue
            number = int(child.split(" ")[0])
            child = " ".join(child.split(" ")[1:])
            parents[child].append(parent)
            children[parent].append([child, number])

    seen = set()
    queue = deque([target])
    while queue:
        current = queue.popleft()
        if current in seen:
            continue
        seen.add(current)
        for parent in parents[current]:
            queue.append(parent)

    def size(bag):
        return 1 + sum(n * size(c) for c, n in children[bag])

    print(size(target) - 1)

    print(len(seen) - 1)

    # def parent_bag(child_bag, multiplier=1):
    #     print(child_bag, multiplier)

    #     parent_content = bags_dict[child_bag]

    #     for content in parent_content:

    #         if "other" in content:
    #             return

    #         print(content)

    #         next_parent = list(content.keys())[0]
    #         parent_value = int(list(content.values())[0])

    #         sum_bag.append(parent_value * multiplier)

    #         parent_bag(next_parent, parent_value * multiplier)

    #     for parent in bags_dict:
    #         content = bags_dict[parent]
    #         if child_bag in content:
    #             parent_bag(parent)
    #             bagset.add(parent)

    #     return

    # for line in input_data:
    #     line = line.replace(" bags", "").replace(" bag", "").replace(".", "")
    #     bag = line.split(" contain ")
    #     bags_dict[bag[0]] = [
    #         {
    #             sub_bag.strip().split(" ", 1)[1]: sub_bag.strip().split(" ", 1)[0]
    #         } for sub_bag in bag[1].split(",")
    #     ]

    # # pprint(bags_dict)

    # a = parent_bag("shiny gold")
    # print(a)
    # # print("Part 1: The amount of different coloured bags that can hold a shiny gold bag: " + str(len(bagset)))


def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2020, 7, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2020, 7)
    part_one(data)
    part_two(data)
