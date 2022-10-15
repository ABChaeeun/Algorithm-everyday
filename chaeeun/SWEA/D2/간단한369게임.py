N = int(input())

for num in range(1, N + 1):

    a = num // 100
    b = num // 10 % 10
    c = num % 10

    if a == 0: a = -1
    if b == 0: b = -1
    if c == 0: c = -1

    a = a % 3
    b = b % 3
    c = c % 3

    # 3이 3개 있을 경우
    if a == 0 and b == 0 and c == 0:
        print('--- ', end='')

    # 3이 2개 있을 경우
    elif a != 0 and b == 0 and c == 0:
        print('-- ', end='')
    elif a == 0 and b != 0 and c == 0:
        print('-- ', end='')
    elif a == 0 and b == 0 and c != 0:
        print('-- ', end='')

    # 3이 1개 있을 경우
    elif a != 0 and b != 0 and c == 0:
        print('- ', end='')
    elif a != 0 and b == 0 and c != 0:
        print('- ', end='')
    elif a == 0 and b != 0 and c != 0:
        print('- ', end='')

    # 3이 0개 있을 경우
    else:
        print('{} '.format(num), end='')
