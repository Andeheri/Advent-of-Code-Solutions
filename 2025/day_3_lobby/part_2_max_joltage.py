
csv_path = "day_3_lobby/input.csv"
delimiter = "\n"

with open(csv_path, 'r') as file:
    banks = file.read().strip().split(delimiter)
print(banks[0])

num_active_batteries = 12

highest_bank_joltages = []
for bank in banks:
    bank_length = len(bank)
    highest_cells = [0 for _ in range(num_active_batteries)]
    for i, cell in enumerate(bank, start = 1):
        value_cell = int(cell)
        for j in range(num_active_batteries):
            if value_cell > highest_cells[j] and bank_length - i >= num_active_batteries - (j + 1):
                highest_cells[j] = value_cell
                for k in range(j + 1, num_active_batteries):
                    highest_cells[k] = 0
                break
    print(f"Bank: {bank}\nHighest cells:")
    print(highest_cells)
    print(f"Joltage value: {sum([value * 10 ** i for i, value in enumerate(highest_cells[::-1])])}\n")
    highest_bank_joltages.append(sum([value * 10 ** i for i, value in enumerate(highest_cells[::-1])]))
print(highest_bank_joltages)
print(f"Sum of highest joltages in each bank: {sum(highest_bank_joltages)}")

2324431343543344443322222212775234334313412212223452223412144123444221524333323312347223423353122242