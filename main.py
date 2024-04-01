import build_list
import find_missing

num_list = 0
missing = 0

num_list = build_list.build_list_of_numbers()
missing = find_missing.find_missing_number(num_list)

print("Missing number in the list: ", missing)
