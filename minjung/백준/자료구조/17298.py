import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
res=[-1]*(n)
stack = []

for i in range(len(nums)):
    while stack and nums[stack[-1]] < nums[i]:
        res[stack.pop()] = nums[i]
    stack.append(i)

print(*res)