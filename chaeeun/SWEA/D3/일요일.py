T = int(input())

lst = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

for tc in range(1, T + 1):
    strr = input()

    if strr != 'SUN':
        print('#{} {}'.format(tc, (6 - lst.index(strr))))
    else:
        print('#{} {}'.format(tc, 7))
