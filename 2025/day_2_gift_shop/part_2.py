
from tqdm import tqdm
from sympy import isprime

csv_path = "day_2_gift_shop/input.csv"
delimiter = ","

with open(csv_path, 'r') as file:
    data = file.read().strip().split(delimiter)

product_IDs = []
for item in data:
    start_id, end_id = item.split("-")
    product_IDs.append((int(start_id), int(end_id)))
print(product_IDs)

def factor_pairs(n: int):
    pairs = [(1, n)]
    # check divisors from 2 up to sqrt(n)
    for a in range(2, int(n**0.5) + 1):
        if n % a == 0:
            b = n // a
            pairs.append((a, b))
            if a != b:
                pairs.append((b, a))
    return pairs


invalid_IDs = []
for start_id, end_id in tqdm(product_IDs):
    start_order = len(str(start_id))
    end_order = len(str(end_id))
    valid_number_of_digits = [i for i in range(start_order, end_order + 1) if i >= 2]
    if not valid_number_of_digits:
        continue
    print(f"Valid number of digits between {start_id} and {end_id}:")
    for num_digits in valid_number_of_digits:
        pairs = factor_pairs(num_digits)
        for prefix_length, repeat_number in pairs:
            possible_prefixes = range(10**(prefix_length - 1), 10**(prefix_length))
            for prefix in possible_prefixes:
                possible_invalid_ID = int(str(prefix) * repeat_number)
                if possible_invalid_ID >= start_id and possible_invalid_ID <= end_id:
                    if possible_invalid_ID in invalid_IDs:
                        continue
                    invalid_IDs.append(possible_invalid_ID)
                    print(f"Found invalid ID between {start_id} and {end_id}: {possible_invalid_ID}")
print(f"Password: {sum(invalid_IDs)}")
