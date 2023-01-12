from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

stack = deque()
for i in range(N):
    stack.append(int(input()))

tmp = []
tmp.append(stack.pop())

while stack:
    # print()
    # print('while stack:')
    # print('stack', *stack)
    # print('tmp', *tmp)
    # print('tmp[-1], stack[-1]', tmp[-1], stack[-1])
    if tmp[-1] >= stack[-1]:
        stack.pop()
    else:
        tmp.append(stack.pop())




# print(*tmp)
print(len(tmp))