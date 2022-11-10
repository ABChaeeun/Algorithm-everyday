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

from collections import deque
 
t = int(input())
 
for i in range(t):
    p = input()
    n = int(input())
    arr = input()[1:-1].split(',')
 
    queue = deque(arr)
 
    flag = 0
 
    if n == 0:
        queue = []
 
    for j in p:
        if j == 'R':
            flag += 1
        elif j == 'D':
            if len(queue) == 0:
                print("error")
                break
            else:
                if flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
 
    else:
        if flag % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")