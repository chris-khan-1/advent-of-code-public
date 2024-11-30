import pytest

from src.aoc_2015.day_19.aoc_2015_19_solution import (
    count_distinct_possible_molecules,
    get_fewest_replacements,
    get_possible_molecules,
    parse_replacement_map,
)


@pytest.fixture(scope="module")
def mock_input():
    return [
        "H => HO",
        "H => OH",
        "O => HH",
    ]


@pytest.fixture(scope="module")
def mock_replacements():
    return [("H", "HO"), ("H", "OH"), ("O", "HH")]


def test_parse_replacement_map(mock_input, mock_replacements):
    actual = parse_replacement_map(input=mock_input)
    assert actual == mock_replacements


def test_get_possible_molecules(mock_replacements):
    actual = get_possible_molecules(
        calibration_molecule="HOH", replacements=mock_replacements
    )
    assert actual == ["HOOH", "HOHO", "OHOH", "HOOH", "HHHH"]


@pytest.mark.parametrize(
    argnames=["molecule", "expected"],
    argvalues=[
        pytest.param("HOH", 4),
        pytest.param("HOHOHO", 7),
    ],
)
def test_count_distinct_possible_molecules(mock_input, molecule, expected):
    actual = count_distinct_possible_molecules(
        input=mock_input, calibration_molecule=molecule
    )
    assert actual == expected


def test_get_fewest_replacements():
    input = [
        "e => H",
        "e => O",
        "H => HO",
        "H => OH",
        "O => HH",
    ]

    actual = get_fewest_replacements(input=input, molecule="HOH")
    assert actual == 3
