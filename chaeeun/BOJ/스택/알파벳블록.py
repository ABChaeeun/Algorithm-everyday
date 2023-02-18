import sys

input = sys.stdin.readline
from collections import deque

answer = deque()
lst = []
n = int(input())
for i in range(n):
    strr = input().split()
    lst.append(int(strr[0]))
    # print(lst)

    if int(strr[0]) == 1:
        answer.append(strr[1])

    elif int(strr[0]) == 2:
        answer.appendleft(strr[1])

    elif int(strr[0]) == 3:
        if len(lst) >= 1:
            lst.pop()
            if len(lst) >= 1:
                if lst[-1] == 1:
                    # print(answer)
                    answer.pop()
                    lst.pop()
                    # answer.pop()
                elif lst[-1] == 2:
                    # print(answer)
                    answer.popleft()
                    lst.pop()
                    # answer.popleft()

if answer:
    print(''.join(answer))
else:
    print(0)
