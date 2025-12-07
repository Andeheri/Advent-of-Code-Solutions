
csv_path = "day_1_secret_entrance\input.csv"
delimiter = "\n"

# Read csv file
with open(csv_path, 'r') as file:
    data = file.read().strip().split(delimiter)
    print(data)

initial_value = 50
zero_count = 0

value = initial_value
for move in data:
    if move[0] == 'R':
        value = (value + int(move[1:])) % 100       
    elif move[0] == 'L':
        value = (value - int(move[1:])) % 100
    if value == 0:
        zero_count += 1


print(f"The password to the safe is: {zero_count}")