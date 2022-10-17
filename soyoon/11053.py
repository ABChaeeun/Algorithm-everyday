n = int(input())
a = input().split()
a = list(int(i) for i in a)

stack = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i]>a[j] and stack[i]<stack[j]:
            stack[i]=stack[j]
    stack[i] += 1
print(max(stack))