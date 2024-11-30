import pytest

from src.aoc_2015.day_07.aoc_2015_07_solution import evaluate, parse_instruction_list


def test_parse_instruction_list():
    instruction_list = [
        "123 -> x",
        "x AND y -> z",
        "p LSHIFT 2 -> q",
        "NOT e -> f",
        "x OR y -> e",
        "y RSHIFT 2 -> g",
    ]
    expected = {
        "x": "123",
        "z": "x AND y",
        "q": "p LSHIFT 2",
        "f": "NOT e",
        "e": "x OR y",
        "g": "y RSHIFT 2",
    }
    actual = parse_instruction_list(instruction_list=instruction_list)
    assert actual == expected


@pytest.fixture(scope="module")
def mock_instructions():
    return {
        "x": "123",
        "y": "456",
        "d": "x AND y",
        "e": "x OR y",
        "f": "x LSHIFT 2",
        "g": "y RSHIFT 2",
        "h": "NOT x",
        "i": "NOT y",
    }


@pytest.mark.parametrize(
    argnames=["input_wire", "expected"],
    argvalues=[pytest.param("x", 123), pytest.param("y", 456)],
)
def test_evaluate_signal_assignment(mock_instructions, input_wire, expected):
    assert evaluate(wire=input_wire, instructions=mock_instructions) == expected


def test_evaluate_bitwise_and(mock_instructions):
    assert evaluate(wire="d", instructions=mock_instructions) == 72


def test_evaluate_bitwise_or(mock_instructions):
    assert evaluate(wire="e", instructions=mock_instructions) == 507


def test_evaluate_bitwise_lshift(mock_instructions):
    assert evaluate(wire="f", instructions=mock_instructions) == 492


def test_evaluate_bitwise_rshift(mock_instructions):
    assert evaluate(wire="g", instructions=mock_instructions) == 114


@pytest.mark.parametrize(
    argnames=["input_wire", "expected"],
    argvalues=[pytest.param("h", 65412), pytest.param("i", 65079)],
)
def test_evaluate_btiwise_not(mock_instructions, input_wire, expected):
    assert evaluate(wire=input_wire, instructions=mock_instructions) == expected
