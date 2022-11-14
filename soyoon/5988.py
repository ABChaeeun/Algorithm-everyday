n = int(input())

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        print('even')
    elif num % 2 == 1:
        print('odd')