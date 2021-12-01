filepath = "input.txt"
input = []

with open(filepath) as file:
    for line in file:
        input.append(int(line.rstrip()))


def find_number_of_decreases(puzzle_input):
    previous = None
    increases_cnt = 0

    for sonar in puzzle_input:
        if previous is None:
            previous = sonar
            continue

        if previous < sonar:
            increases_cnt += 1

        previous = sonar

    return increases_cnt


print(find_number_of_decreases(input))
