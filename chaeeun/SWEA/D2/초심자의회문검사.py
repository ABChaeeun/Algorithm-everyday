T = int(input())

for tc in range(1, T+1):
    strr = input()
    k = len(strr) - 1
    # print(k)
    cnt = 0
    for i in range((len(strr)+1) // 2):
        # print(i, k-i)
        if strr[i] == strr[k-i]:
            cnt += 1

    # print(cnt)
    # print((len(strr)+1) // 2)

    if cnt == ((len(strr)+1) // 2):
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))