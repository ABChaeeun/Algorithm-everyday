import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)

for i in range(len(data)):
    data[i] += (i+1)

print(max(data) + 1)

# 4 3 3 2
# 1 2 3 4

# 5 5 6 6

# 39 39 38 35 29 9
# 1  2  3  4  5  6
# 41+1
