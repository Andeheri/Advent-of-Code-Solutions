
csv_path = '2018/day_1/input.csv'
delimiter = '\n'

with open(csv_path) as f:
    data = f.read().strip().split(delimiter)

result = 0
seen_numbers = {0}
running = True
while running:
    for line in data:
        if line[0] == '+':
            result += int(line[1:])
        else:
            result -= int(line[1:])
        if result in seen_numbers:
            running = False
            break
        seen_numbers.add(result)
print(f"The following frequency is reached twice: {result}")