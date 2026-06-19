arr = [1,2,3,4,5,5,6,6,6,6,6]
seen = {}
for num in arr:
    if num in seen:
        seen[num] += 1
    else:
        seen[num] = 1
print(seen)