import sys

N = int(sys.stdin.readline())

### 메모리 초과
# lst = []
# for i in range(N):
#     lst.append(int(input()))
# lst.sort()
# for i in range(N):
#     print(lst[i])

### input() -> 시간초과

### sys.stdin.readline() -> 성공
lst = [0] * 10001

for i in range(N):
    lst[int(sys.stdin.readline())] += 1

for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)
