from collections import defaultdict
from itertools import permutations


def parse_distances(route_list: list[str]) -> dict:
    routes = defaultdict(dict)
    for route in route_list:
        start, _, destination, _, distance = route.split(" ")
        routes[start][destination] = int(distance)
        routes[destination][start] = int(distance)
    return routes


def get_all_routes(route_info: dict) -> list[tuple]:
    cities = route_info.keys()
    return list(permutations(cities))


def get_route_distance(route: tuple, route_info: dict) -> int:
    distance = 0
    for i in range(len(route) - 1):
        distance += route_info[route[i]][route[i + 1]]
    return distance


def get_shortest_route(route_info: dict) -> int | float:
    all_routes = get_all_routes(route_info=route_info)
    shortest_distance = float("inf")
    for route in all_routes:
        route_distance = get_route_distance(route=route, route_info=route_info)
        if route_distance < shortest_distance:
            shortest_distance = route_distance
    return shortest_distance


def get_longest_route(route_info: dict) -> int:
    all_routes = get_all_routes(route_info=route_info)
    longest_distance = 0
    for route in all_routes:
        route_distance = get_route_distance(route=route, route_info=route_info)
        if route_distance > longest_distance:
            longest_distance = route_distance
    return longest_distance


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2015/day_09/input.txt"
    result_path = "./src/aoc_2015/day_09/result.txt"

    string_input = helpers.read_file(file_path=input_path)

    route_info = parse_distances(
        route_list=helpers.read_file_lines(file_path=input_path)
    )
    shortest_route = get_shortest_route(route_info=route_info)
    longest_route = get_longest_route(route_info=route_info)

    result = f"""\
        Part 1: The shortest route is {shortest_route}.
        Part 2: the longest route is {longest_route}.
        """

    helpers.write_file(file_path=result_path, contents=result)
