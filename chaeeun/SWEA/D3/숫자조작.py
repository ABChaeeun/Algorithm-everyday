def swap(lst_tmp, a, b):
    tmp = lst_tmp[a]
    lst_tmp[a] = lst_tmp[b]
    lst_tmp[b] = tmp


T = int(input())
for tc in range(1, T + 1):

    lst = list()
    num = input()
    for i in num:
        lst.append(int(i))

    max = int(''.join(map(str, lst)))
    min = int(''.join(map(str, lst)))
    for i in range(len(lst)):
        for j in range(len(lst)):
            lst_tmp = lst.copy()
            swap(lst_tmp, i, j)
            if max < int(''.join(map(str, lst_tmp))):
                max = int(''.join(map(str, lst_tmp)))
            if lst_tmp[0] != 0:  # 맨 앞 0 체크는 여기서 이렇게 체크해주면 됐다!!!
                if min > int(''.join(map(str, lst_tmp))):
                    print(*lst_tmp)
                    min = int(''.join(map(str, lst_tmp)))

    print('#{} {} {}'.format(tc, min, max))
