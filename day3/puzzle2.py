filepath = "input.txt"
puzzle_input = []

with open(filepath) as file:
    for line in file:
        puzzle_input.append(line.rstrip())


def find_most_common_least_common(numbers):
    most_common = []
    least_common = []

    for i in range(len(numbers[0])):
        most_common.append(0)
        least_common.append(0)

    for binary in numbers:
        for idx, bit in enumerate(binary):
            if bit == '1':
                most_common[idx] += 1
            else:
                most_common[idx] -= 1

    for idx, num in enumerate(most_common):
        if num >= 0:
            most_common[idx] = 1
            least_common[idx] = 0
        else:
            most_common[idx] = 0
            least_common[idx] = 1

    return [most_common, least_common]


def find_rating(numbers, mode):
    most_common_least_common = find_most_common_least_common(numbers)
    result_set = numbers
    new_result_set = []

    for i in range(len(numbers[0])):
        for num in result_set:
            if int(num[i]) == most_common_least_common[0 if mode == "oxygen" else 1][i]:
                new_result_set.append(num)

        if len(new_result_set) == 1:
            return int(new_result_set[0], 2)

        result_set = new_result_set.copy()
        new_result_set = []
        most_common_least_common = find_most_common_least_common(result_set)


def most_common_to_binary(common):
    binary = ""
    binary_inverse = ""
    for num in common:
        binary += str(num)
        binary_inverse += str(1-num)

    return [binary, binary_inverse]


oxygen = find_rating(puzzle_input, "oxygen")
co2 = find_rating(puzzle_input, "co2")

print("oxygen", oxygen)
print("co2", co2)

print("multiplied", oxygen*co2)
