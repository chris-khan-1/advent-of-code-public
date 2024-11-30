import pytest

from src.aoc_2015.day_09.aoc_2015_09_solution import (
    get_all_routes,
    get_longest_route,
    get_route_distance,
    get_shortest_route,
    parse_distances,
)


@pytest.fixture(scope="module")
def mock_route_info():
    return {
        "London": {"Dublin": 464, "Belfast": 518},
        "Dublin": {"London": 464, "Belfast": 141},
        "Belfast": {"London": 518, "Dublin": 141},
    }


def test_parse_distances(mock_route_info):
    input = [
        "London to Dublin = 464",
        "London to Belfast = 518",
        "Dublin to Belfast = 141",
    ]
    expected = mock_route_info
    actual = parse_distances(route_list=input)
    assert actual == expected


def test_get_all_routes(mock_route_info):
    actual = get_all_routes(route_info=mock_route_info)
    expected = [
        ("Dublin", "London", "Belfast"),
        ("London", "Dublin", "Belfast"),
        ("London", "Belfast", "Dublin"),
        ("Dublin", "Belfast", "London"),
        ("Belfast", "Dublin", "London"),
        ("Belfast", "London", "Dublin"),
    ]
    assert set(actual) == set(expected)  # list order doesn't matter


@pytest.mark.parametrize(
    argnames=["route", "expected"],
    argvalues=[
        pytest.param(["Dublin", "London", "Belfast"], 982),
        pytest.param(["London", "Dublin", "Belfast"], 605),
    ],
)
def test_get_route_distance(mock_route_info, route, expected):
    actual = get_route_distance(route=route, route_info=mock_route_info)
    assert actual == expected


def test_get_shortest_route(mock_route_info):
    assert get_shortest_route(route_info=mock_route_info) == 605


def test_get_longest_route(mock_route_info):
    assert get_longest_route(route_info=mock_route_info) == 982
