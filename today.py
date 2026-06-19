def check_duplicates(input_list):
    duplicates = []
    seen = set()
    
    for item in input_list:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    
    return duplicates

check_list = list(map(int, input("").split()))
duplicate_values = check_duplicates(check_list)
print(duplicate_values)