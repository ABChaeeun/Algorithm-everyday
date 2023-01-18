import sys
input = sys.stdin.readline

lst = []
for i in range(9):
    lst.append(int(input()))

two_sum = 0
a = 0
b = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        two_sum = lst[i] + lst[j]
        if lst[i] != lst[j] and two_sum == sum(lst) - 100:
            a = lst[i]
            b = lst[j]
            # print(a, b)
            break

lst.sort()
for i in range(9):
    if lst[i] != a and lst[i] != b:
        print(lst[i])