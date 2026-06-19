# arr = list(map(int,input().split()))
# print(arr)

# matrix = []
# for i in range(3):  
#     row = list(map(int,input().split()))
#     matrix.append(row)

# max_element = matrix[0][0]
# for row in matrix:   #O(n^2)
#     for element in row:
#         if element > max_element:
#             max_element = element

# print(max_element)


# n = int(input())
# x = str(n)
# ans = len(x)
# print(ans)


n = int(input())
cnt = 1
while n >= 10:
    n //= 10
    cnt += 1
print(cnt)