def parse_instruction_list(instruction_list: list) -> dict:
    instructions = dict()
    for instruction in instruction_list:
        operation, output_wire = instruction.split(" -> ")
        instructions[output_wire] = operation
    return instructions


def evaluate(wire: str, instructions: dict, wire_cache: dict = {}):
    if wire.isdigit():
        return int(wire)
    if wire in wire_cache:
        return wire_cache[wire]

    instruction = instructions[wire]

    parts = instruction.split(" ")

    if "AND" in parts:
        left = evaluate(wire=parts[0], instructions=instructions, wire_cache=wire_cache)
        right = evaluate(
            wire=parts[2], instructions=instructions, wire_cache=wire_cache
        )
        result = left & right
    elif "OR" in parts:
        left = evaluate(wire=parts[0], instructions=instructions, wire_cache=wire_cache)
        right = evaluate(
            wire=parts[2], instructions=instructions, wire_cache=wire_cache
        )
        result = left | right
    elif "LSHIFT" in parts:
        left = evaluate(wire=parts[0], instructions=instructions, wire_cache=wire_cache)
        shift_ammount = int(parts[2])
        result = left << shift_ammount
    elif "RSHIFT" in parts:
        left = evaluate(wire=parts[0], instructions=instructions, wire_cache=wire_cache)
        shift_ammount = int(parts[2])
        result = left >> shift_ammount
    elif "NOT" in parts:
        value = evaluate(
            wire=parts[1], instructions=instructions, wire_cache=wire_cache
        )
        result = ~value & 0xFFFF
    else:
        result = evaluate(
            wire=parts[0], instructions=instructions, wire_cache=wire_cache
        )

    wire_cache[wire] = result
    return result


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers  # noqa: E402

    input_path = "./src/aoc_2015/day_07/input.txt"
    result_path = "./src/aoc_2015/day_07/result.txt"

    instruction_list = helpers.read_file_lines(file_path=input_path)

    instructions = parse_instruction_list(instruction_list)
    # Part 1
    wire_a_signal = evaluate(wire="a", instructions=instructions, wire_cache={})
    # Part 2
    instructions["b"] = str(wire_a_signal)
    new_wire_a_signal = evaluate(wire="a", instructions=instructions, wire_cache={})

    result = f"""\
        Part 1: The signal provided to wire a is {wire_a_signal}
        Part 2: The new signal provided to wire a is {new_wire_a_signal}
        """

    helpers.write_file(file_path=result_path, contents=result)
