from src.aoc_2015.day_16.aoc_2015_16_solution import (
    check_sue,
    check_sue_updated,
    get_correct_sue,
    parse_sue_info,
)


def test_parse_sue_info():
    expected = {
        "1": {
            "children": None,
            "cats": None,
            "samoyeds": None,
            "pomeranians": None,
            "akitas": 0,
            "vizslas": None,
            "goldfish": 6,
            "trees": 9,
            "cars": None,
            "perfumes": None,
        },
        "3": {
            "children": None,
            "cats": None,
            "samoyeds": None,
            "pomeranians": None,
            "akitas": 6,
            "vizslas": None,
            "goldfish": None,
            "trees": None,
            "cars": 10,
            "perfumes": 7,
        },
    }
    actual = parse_sue_info(
        input=[
            "Sue 1: goldfish: 6, trees: 9, akitas: 0",
            "Sue 3: cars: 10, akitas: 6, perfumes: 7",
        ]
    )
    assert actual == expected


def test_check_sue_success():
    actual = check_sue(
        individual_sue_info={
            "children": None,
            "cats": None,
            "samoyeds": None,
            "pomeranians": None,
            "akitas": 0,
            "vizslas": None,
            "goldfish": 6,
            "trees": 9,
            "cars": None,
            "perfumes": None,
        },
        test_results={
            "children": 1,
            "cats": 2,
            "samoyeds": 3,
            "pomeranians": 4,
            "akitas": 0,
            "vizslas": 5,
            "goldfish": 6,
            "trees": 9,
            "cars": 4,
            "perfumes": 2,
        },
    )
    assert actual is True


def test_check_sue_not_her():
    # akitas don't match
    actual = check_sue(
        individual_sue_info={
            "children": None,
            "cats": None,
            "samoyeds": None,
            "pomeranians": None,
            "akitas": 5,
            "vizslas": None,
            "goldfish": 6,
            "trees": 9,
            "cars": None,
            "perfumes": None,
        },
        test_results={
            "children": 1,
            "cats": 2,
            "samoyeds": 3,
            "pomeranians": 4,
            "akitas": 0,
            "vizslas": 5,
            "goldfish": 6,
            "trees": 9,
            "cars": 4,
            "perfumes": 2,
        },
    )
    assert actual is False


def test_get_correct_sue():
    input = [
        "Sue 1: goldfish: 6, trees: 9, akitas: 0",
        "Sue 3: cars: 10, akitas: 6, perfumes: 7",
    ]
    test_results = {
        "children": 1,
        "cats": 2,
        "samoyeds": 3,
        "pomeranians": 4,
        "akitas": 6,
        "vizslas": 5,
        "goldfish": 6,
        "trees": 9,
        "cars": 10,
        "perfumes": 7,
    }
    actual = get_correct_sue(input=input, test_results=test_results)
    assert actual == "3"


def test_check_sue_updated_fail():
    actual = check_sue_updated(
        individual_sue_info={
            "children": None,
            "cats": None,
            "samoyeds": None,
            "pomeranians": None,
            "akitas": 0,
            "vizslas": None,
            "goldfish": 6,
            "trees": 8,
            "cars": None,
            "perfumes": None,
        },
        test_results={
            "children": 1,
            "cats": 2,
            "samoyeds": 3,
            "pomeranians": 4,
            "akitas": 0,
            "vizslas": 5,
            "goldfish": 6,
            "trees": 9,
            "cars": 4,
            "perfumes": 2,
        },
    )
    assert actual is False
