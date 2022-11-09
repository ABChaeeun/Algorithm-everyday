t = int(input())

for i in range(t):
    test_case = input().split(' ')
    for j in test_case:
        print(j[::-1], end=' ')
