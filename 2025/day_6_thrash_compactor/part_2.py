
csv_path = "day_6_thrash_compactor/input.csv"
delimiter = "\n"

with open(csv_path, "r") as file:
    lines = file.read().strip().split(delimiter)

number_lines, operator_line = lines[:-1], lines[-1]

groups = []

split_indexes = []
new_operator_line = []

for i, char in enumerate(operator_line, start = -1):
    if char != ' ':
        split_indexes.append(i)
        new_operator_line.append(char)
split_indexes = split_indexes[1:]
operator_line = new_operator_line

for i, line in enumerate(number_lines):
    splitted_line = []
    prev_index = 0
    for split_index in split_indexes:
        splitted_line.append(line[prev_index: split_index])
        prev_index = split_index + 1
    if prev_index < len(line):
        splitted_line.append(line[prev_index:])
    number_lines[i] = splitted_line


def multiply_numbers(numbers: list[int]) -> int:
    result = 1
    for number in numbers:
        result *= number
    return result


def add_numbers(numbers: list[int]) -> int:
    result = 0
    for number in numbers:
        result += number
    return result


def construct_cephalopod_numbers(numbers: list[str]) -> list[int]:
    cephalopod_numbers = []
    for digits in zip(*numbers):
        cephalopod_number = ''
        for digit in digits:
            if digit != ' ':
                cephalopod_number += digit
        cephalopod_numbers.append(int(cephalopod_number))
    return cephalopod_numbers

result = 0
for (*numbers, operator) in zip(*number_lines, operator_line):
    numbers = construct_cephalopod_numbers(numbers)
    match operator:
        case '+':
            result += add_numbers(numbers)
        case '*':
            result += multiply_numbers(numbers)

print(f"The answer is: {result}")