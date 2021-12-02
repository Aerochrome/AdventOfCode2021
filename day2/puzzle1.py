filepath = "input.txt"
puzzle_input = []

with open(filepath) as file:
    for line in file:
        puzzle_input.append(line.rstrip())


def run_instructions(instructions):
    state = {
        'x': 0,
        'y': 0
    }

    for instruction in instructions:
        splitted = instruction.split(" ", 2)
        run_instruction(splitted[0], int(splitted[1]), state)

    return state


def run_instruction(instruction, value, state):
    if instruction == "up":
        state['y'] -= value
    elif instruction == "down":
        state['y'] += value
    elif instruction == "forward":
        state['x'] += value


def multiply_state(state):
    return state['x'] * state['y']


result_state = run_instructions(puzzle_input)
print(multiply_state(result_state))
