arr = list(map(int,input().split()))
n = len(arr)    
mpp = {}
res = []
for num in arr:
    if num in mpp:
        mpp[num] += 1
    else:
        mpp[num] = 1
for num in mpp:
    if mpp[num] > (n//3):
        res.append(num)
print(res)

