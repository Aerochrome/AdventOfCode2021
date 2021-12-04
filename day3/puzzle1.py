filepath = "input.txt"
puzzle_input = []

with open(filepath) as file:
    for line in file:
        puzzle_input.append(line.rstrip())


def find_most_common(numbers):
    most_common = []

    for i in range(len(numbers[0])):
        most_common.append(0)

    for binary in numbers:
        for idx, bit in enumerate(binary):
            if bit == '1':
                most_common[idx] += 1
            else:
                most_common[idx] -= 1

    return most_common


def most_common_to_binary(common):
    binary = ""
    binary_inverse = ""
    for num in common:
        if num > 0:
            binary += "1"
            binary_inverse += "0"
        else:
            binary += "0"
            binary_inverse += "1"

    return [binary, binary_inverse]


common = find_most_common(puzzle_input)
res_bin = most_common_to_binary(common)

res_dec = [int(res_bin[0], 2), int(res_bin[1], 2)]

print('Gamma', res_dec[0])
print('Epsilon', res_dec[1])

print('Multiplied', res_dec[0]*res_dec[1])
