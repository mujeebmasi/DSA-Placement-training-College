arr = [1,1,2,3,4,5,6,6]
mpp = {}
res = []

for num in arr:
    if num not in mpp:
        res.append(num)
    mpp[num] = 1
print(res)

seen = set()
res2 = []

for num in arr:
    if num not in seen:
        res2.append(num)
        seen.add(num)
print(res2)
    

