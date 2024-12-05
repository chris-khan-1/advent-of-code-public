from src.aoc_2015.day_17.aoc_2015_17_solution import (
    get_combinations,
    get_min_container_combinations,
    get_total_combinations,
)


def test_get_combinations():
    acutal = get_combinations(containers=[20, 15, 10, 5, 5], total_size=25)
    assert set(acutal) == {(20, 5), (20, 5), (15, 10), (15, 5, 5)}


def test_get_total_combinations():
    actual = get_total_combinations(containers=[20, 15, 10, 5, 5], total_size=25)
    assert actual == 4


def test_get_min_container_combinations():
    acutal = get_min_container_combinations(
        containers=[20, 15, 10, 5, 5], total_size=25
    )
    assert set(acutal) == {(20, 5), (20, 5), (15, 10)}
