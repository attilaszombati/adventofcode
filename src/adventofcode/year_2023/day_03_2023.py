from collections import defaultdict

import math

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2023, 3, 1)
def part_one(input_data: list[str]):
    matrix = [[x for x in line] for line in input_data]

    children = defaultdict(list)
    parents = set()

    def river_sizes_dfs(matrix):

        def append_river(i, j, parent):

            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and (i, j) not in parents and matrix[i][j] != ".":
                if matrix[i][j] != ".":
                    parents.add((i, j))
                    children[parent].append((i, j))
                    yield from append_river(i, j + 1, parent=parent)
                    yield from append_river(i + 1, j, parent=parent)
                    yield from append_river(i + 1, j + 1, parent=parent)
                    yield from append_river(i - 1, j + 1, parent=parent)
                    yield from append_river(i, j - 1, parent=parent)
                    yield from append_river(i - 1, j, parent=parent)
                    yield from append_river(i - 1, j - 1, parent=parent)
                    yield from append_river(i + 1, j - 1, parent=parent)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "*":
                    parent = (i, j)
                    yield from append_river(i, j, parent=parent)

                    children[parent].remove(parent)

                    new_points = []
                    from collections import deque

                    sorted_children = sorted(children[parent])

                    queue = deque(sorted_children)

                    while queue:
                        next_elem = queue.popleft()
                        sub_points = [next_elem]
                        copy = queue.copy()
                        for elem in copy:
                            if math.dist(sub_points[-1], elem) == 1.0:
                                sub_points.append(elem)
                                queue.remove(elem)

                        new_points.append(sub_points)

                    children[parent] = new_points

        return

    yield from river_sizes_dfs(matrix)
    sum_num = []

    for child in children:

        if len(children[child]) == 1:
            continue

        # for sort in children[child]:
#
        #     number = "".join([matrix[x][y] for x, y in sort])
#
        #     sum_num.append(int(number))

        number_1 = "".join([matrix[x][y] for x, y in children[child][0]])
        number_2 = "".join([matrix[x][y] for x, y in children[child][1]])
        sum_num.append(int(number_1) * int(number_2))

    yield sum(sum_num)


@register_solution(2023, 3, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2023, 3, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 3)
    part_one = list(part_one(data))[0]
    print(part_one)
    # part_two(data)
