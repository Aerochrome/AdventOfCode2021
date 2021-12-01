filepath = "input.txt"
input = []

with open(filepath) as file:
    for line in file:
        input.append(int(line.rstrip()))


def find_number_of_decreases_three_measurement(puzzle_input):
    groups = []
    increases_cnt = 0

    for idx, sonar in enumerate(puzzle_input):

        groups.append([])

        groups[idx].append(sonar)

        if (idx-1) > -1:
            groups[idx-1].append(sonar)

        if (idx-2) > -1:
            groups[idx-2].append(sonar)

    prev_group = None
    for group in groups:
        if prev_group is None:
            prev_group = group
            continue

        if sum(prev_group) < sum(group):
            increases_cnt += 1

        prev_group = group

    return increases_cnt


print(find_number_of_decreases_three_measurement(input))
