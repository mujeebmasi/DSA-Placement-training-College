# arr = list(map(int,input().split()))
# n = len(arr)
# arr1 = []
# arr2 = []
# for num in arr:
#     if num&1 == 1:  #odd
#         arr2.append(num)
#     else:
#         arr1.append(num)
# res = arr1+arr2
# print(*res)

# 120 11 42 55 34
# 120 11 42 34 55



nums = list(map(int,input().split()))
n = len(nums)
new_nums = []
for i in range(n-1):
    if nums[i]%10 > nums[i+1]%10:
        nums[i],nums[i+1] = nums[i+1],nums[i]

print(*nums)
    

    


