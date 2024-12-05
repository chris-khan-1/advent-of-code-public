import pytest

from src.aoc_2015.day_14.aoc_2015_14_solution import (
    get_distance_given_time,
    get_winning_distance,
    get_winning_points,
    parse_raw_reindeer_info,
)


@pytest.fixture(scope="module")
def mock_input():
    return [
        "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
        "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
    ]


@pytest.fixture(scope="module")
def mock_reindeer_info():
    return {
        "Comet": {"fly_time": 10, "rest_time": 127, "speed": 14},
        "Dancer": {"fly_time": 11, "rest_time": 162, "speed": 16},
    }


def test_parse_raw_reindeer_info(mock_input, mock_reindeer_info):
    actual = parse_raw_reindeer_info(input=mock_input)
    assert actual == mock_reindeer_info


@pytest.mark.parametrize(
    argnames=["reindeer", "time", "expected"],
    argvalues=[
        pytest.param("Comet", 10, 140),
        pytest.param("Comet", 11, 140),
        pytest.param("Comet", 1000, 1120),
        pytest.param("Dancer", 10, 160),
        pytest.param("Dancer", 11, 176),
        pytest.param("Dancer", 1000, 1056),
    ],
)
def test_get_distance_given_time(mock_reindeer_info, reindeer, time, expected):
    actual = get_distance_given_time(
        reindeer_info=mock_reindeer_info, reindeer=reindeer, time=time
    )
    assert actual == expected


def test_get_winning_distance(mock_input):
    actual = get_winning_distance(input=mock_input, time=1000)
    assert actual == 1120


@pytest.mark.parametrize(
    argnames=["time", "expected"],
    argvalues=[
        pytest.param(1, 1),
        pytest.param(2, 2),
        pytest.param(140, 139),
        pytest.param(1000, 689),
    ],
)
def test_get_winning_points(mock_input, time, expected):
    actual = get_winning_points(input=mock_input, time=time)
    assert actual == expected
