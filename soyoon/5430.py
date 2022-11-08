# # 시간초과

# t = int(input())
 
# for i in range(t):
#     p = input()
#     n = int(input())
#     arr = list(map(int,input()[1:-1].replace(',', '')))
 
#     for i in p:
#         if i == 'R':
#             arr = arr[::-1]
#         elif i == "D":
#             if len(arr) == 0:
#                 break
#             else:
#                 arr.pop(0)
#     if arr == []:
#         print('error')
#     else:
#         print(arr)  
arr = input()[1:-1].split(',')
print(arr)