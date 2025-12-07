csv_path = "day_1_secret_entrance\\input.csv"
delimiter = "\n"

with open(csv_path, 'r') as file:
    data = file.read().strip().split(delimiter)

initial_value = 50
zero_count = 0
value = initial_value

for move in data:
    change = int(move[1:])
    zero_count += change // 100          # full 100-click loops
    rem = change % 100                   # remaining clicks

    if move[0] == 'R':
        new_value = (value + rem) % 100
        # Hit 0 iff we wrapped once in the remainder
        if rem > 0 and new_value < value:
            zero_count += 1

    else:  # 'L'
        new_value = (value - rem) % 100
        # Hit 0 iff value > 0 and we had enough clicks to reach it
        if value > 0 and rem >= value:
            zero_count += 1

    value = new_value

print(f"The password to the secret entrance is: {zero_count}")
