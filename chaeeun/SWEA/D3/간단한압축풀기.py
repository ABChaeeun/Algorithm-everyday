T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list()
    for i in range(N):
        alph, num = input().split()
        for j in range(int(num)):
            lst.append(alph)

    print('#{}'.format(tc))
    for i in range(len(lst)):
        print(lst[i], sep='', end='')
        if (i+1)%10 == 0:
            print()
    print()