
csv_path = "day_3_lobby/input.csv"
delimiter = "\n"

with open(csv_path, 'r') as file:
    banks = file.read().strip().split(delimiter)
print(banks[0])
highest_bank_joltages = []
for bank in banks:
    bank_length = len(bank)
    highest_first, highest_second = 0, 0
    for i, cell in enumerate(bank, start = 1):
        value_cell = int(cell)
        if value_cell > highest_first and i != bank_length:
            highest_first = value_cell
            highest_second = 0
        else:
            if value_cell > highest_second:
                highest_second = value_cell
    highest_bank_joltages.append(highest_first * 10 +  highest_second)
print(highest_bank_joltages)
print(f"Sum of highest joltages in each bank: {sum(highest_bank_joltages)}")