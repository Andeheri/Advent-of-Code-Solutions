
from tqdm import tqdm

csv_path = "day_2_gift_shop/input.csv"
delimiter = ","

with open(csv_path, 'r') as file:
    data = file.read().strip().split(delimiter)

product_IDs = []
for item in data:
    start_id, end_id = item.split("-")
    product_IDs.append((int(start_id), int(end_id)))
print(product_IDs)


invalid_IDs = []
for start_id, end_id in tqdm(product_IDs):
    start_order = len(str(start_id))
    end_order = len(str(end_id))
    valid_number_of_digits = [i for i in range(start_order, end_order + 1) if i % 2 == 0]
    if not valid_number_of_digits:
        continue
    for num_digits in valid_number_of_digits:
        possible_prefixes = range(10**(num_digits//2 - 1), 10**(num_digits//2))
        for prefix in possible_prefixes:
            possible_invalid_ID = prefix + prefix * 10**(num_digits//2)
            if possible_invalid_ID >= start_id and possible_invalid_ID <= end_id:
                invalid_IDs.append(possible_invalid_ID)
                print(f"Found invalid ID between {start_id} and {end_id}: {possible_invalid_ID}")
    print(f"Password: {sum(invalid_IDs)}")
