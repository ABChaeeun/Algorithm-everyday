T = int(input())

for tc in range(1, T+1):
    str = input()

    ### ver1 - 실패
    # cnt = 0
    # for i in range(11):
    #     if str[i] == str[0]:
    #         for j in range(i):
    #             if str[j] == str[i+j]:
    #                 cnt += 1
    #                 if cnt == 1:
    #                     # 따로 처리...
    #     if cnt != 0:
    #         break
    
    # print(cnt)



    ### ver2 - 성공
    # print(str[0:5])
    # for i in range(1, 12):
    #     if str[i] == str[0]:
    #         if str[0:i] in str:
    #             if str[i:i+i] in str[0:i]:
    #                 print('   ', end='')
    #                 print(str[0:i])
    #                 print(len(str[0:i]))
    #                 print(i)
    #                 break



    ### ver3 - 프린트 포멧만 변경
    for i in range(1, 12):
        if str[i] == str[0]:
            if str[0:i] in str:
                if str[i:i+i] in str[0:i]:
                    print('#{} {}'.format(tc, i))
                    break
