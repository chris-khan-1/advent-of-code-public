from textwrap import dedent

import pytest

from src.aoc_2024.day_05.aoc_2024_05_solution import (
    check_update,
    get_correct_and_incorrect_updates,
    get_correct_updates_total,
    get_corrected_update,
    get_corrected_updates_total,
    get_rule_cache,
    parse_rules_and_updates,
)

mock_input = dedent(
    """\
        47|53
        97|13
        97|61
        97|47
        75|29
        61|13
        75|53
        29|13
        97|29
        53|29
        61|53
        97|53
        61|29
        47|13
        75|47
        97|75
        47|61
        75|61
        47|29
        75|13
        53|13

        75,47,61,53,29
        97,61,53,29,13
        75,29,13
        75,97,47,61,53
        61,13,29
        97,13,75,29,47"""
)

mock_rules = [
    [47, 53],
    [97, 13],
    [97, 61],
    [97, 47],
    [75, 29],
    [61, 13],
    [75, 53],
    [29, 13],
    [97, 29],
    [53, 29],
    [61, 53],
    [97, 53],
    [61, 29],
    [47, 13],
    [75, 47],
    [97, 75],
    [47, 61],
    [75, 61],
    [47, 29],
    [75, 13],
    [53, 13],
]

mock_rule_cache = {
    (47, 53): -1,
    (53, 47): 1,
    (97, 13): -1,
    (13, 97): 1,
    (97, 61): -1,
    (61, 97): 1,
    (97, 47): -1,
    (47, 97): 1,
    (75, 29): -1,
    (29, 75): 1,
    (61, 13): -1,
    (13, 61): 1,
    (75, 53): -1,
    (53, 75): 1,
    (29, 13): -1,
    (13, 29): 1,
    (97, 29): -1,
    (29, 97): 1,
    (53, 29): -1,
    (29, 53): 1,
    (61, 53): -1,
    (53, 61): 1,
    (97, 53): -1,
    (53, 97): 1,
    (61, 29): -1,
    (29, 61): 1,
    (47, 13): -1,
    (13, 47): 1,
    (75, 47): -1,
    (47, 75): 1,
    (97, 75): -1,
    (75, 97): 1,
    (47, 61): -1,
    (61, 47): 1,
    (75, 61): -1,
    (61, 75): 1,
    (47, 29): -1,
    (29, 47): 1,
    (75, 13): -1,
    (13, 75): 1,
    (53, 13): -1,
    (13, 53): 1,
}

mock_correct_updates = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
]

mock_incorrect_updates = [
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47],
]


def test_parse_rules_and_updates():
    input = mock_input

    actual_rules, actual_updates = parse_rules_and_updates(input=input)

    expected_rules = mock_rules
    expected_updates = [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ]

    assert actual_rules == expected_rules
    assert actual_updates == expected_updates


def test_get_rule_cache():
    actual = get_rule_cache(rules=mock_rules)
    expected = mock_rule_cache
    assert actual == expected


def test_get_correct_and_incorrect_updates():
    actual_correct, actual_incorrect, actual_rule_cache = (
        get_correct_and_incorrect_updates(input=mock_input)
    )

    assert actual_correct == mock_correct_updates
    assert actual_incorrect == mock_incorrect_updates
    assert actual_rule_cache == mock_rule_cache


@pytest.mark.parametrize(
    argnames=["input_update", "expected"],
    argvalues=[
        pytest.param([75, 47, 61, 53, 29], True),
        pytest.param([97, 61, 53, 29, 13], True),
        pytest.param([75, 29, 13], True),
        pytest.param([75, 97, 47, 61, 53], False),
        pytest.param([61, 13, 29], False),
        pytest.param([97, 13, 75, 29, 47], False),
    ],
)
def test_check_update(input_update, expected):
    actual = check_update(update=input_update, rule_cache=mock_rule_cache)
    assert actual is expected


def test_get_correct_updates_total():
    actual = get_correct_updates_total(
        correct_updates=mock_correct_updates, rule_cache=mock_rule_cache
    )
    assert actual == 143


@pytest.mark.parametrize(
    argnames=["input_update", "expected"],
    argvalues=[
        pytest.param([75, 97, 47, 61, 53], [97, 75, 47, 61, 53]),
        pytest.param([61, 13, 29], [61, 29, 13]),
        pytest.param([97, 13, 75, 29, 47], [97, 75, 47, 29, 13]),
    ],
)
def test_get_corrected_update(input_update, expected):
    actual = get_corrected_update(update=input_update, rule_cache=mock_rule_cache)
    assert actual == expected


def test_get_corrected_total():
    actual = get_corrected_updates_total(
        incorrect_updates=mock_incorrect_updates, rule_cache=mock_rule_cache
    )
    assert actual == 123
