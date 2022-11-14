T = int(input())
for tc in range(1, T+1):
    strr = input()
    result_strr = list()

    for i in range(len(strr)):
        if strr[i] == 'b':
            result_strr.append('d')
        elif strr[i] == 'd':
            result_strr.append('b')
        elif strr[i] == 'p':
            result_strr.append('q')
        elif strr[i] == 'q':
            result_strr.append('p')

    print('#{} '.format(tc), end='')
    for ii in range(len(strr)-1, -1, -1):
        print(result_strr[ii], sep='', end='')
    print()
