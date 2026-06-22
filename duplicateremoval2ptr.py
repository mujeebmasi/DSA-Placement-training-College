arr = [1,2,3,4,4,5,5,5]
n = len(arr)


res = []

for i in range(n-1):
    if arr[i] != arr[i+1]:
        res.append(arr[i])
res.append(arr[-1])
print(res)
    
        
        
        