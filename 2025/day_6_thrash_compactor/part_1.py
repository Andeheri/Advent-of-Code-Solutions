
csv_path = "day_6_thrash_compactor/input.csv"
delimiter = "\n"

with open(csv_path, "r") as file:
    lines = file.read().strip().split(delimiter)

number_lines, operator_line = lines[:-1], lines[-1]

groups = []

for i, line in enumerate(lines):
    line = line.split(' ')
    line = list(filter(lambda x: x != '', line))
    lines[i] = line


def multiply_numbers(numbers: list) -> int:
    result = 1
    for number in numbers:
        result *= int(number)
    return result


def add_numbers(numbers: list) -> int:
    result = 0
    for number in numbers:
        result += int(number)
    return result


result = 0
for (*numbers, operator) in zip(*lines):
    match operator:
        case '+':
            result += add_numbers(numbers)
        case '*':
            result += multiply_numbers(numbers)

print(f"The answer is: {result}")