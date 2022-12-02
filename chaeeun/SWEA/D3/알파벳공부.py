T = int(input())

for tc in range(1, T + 1):
    strr = input()

    ### ver1 - 그냥 엔터 친 값으로 들어가면 배열 strr 자체가 배열이 아니므로 if 조건에서 에러
    # cnt = 1
    # if strr[0] == 'a':
    #     for i in range(0, len(strr) - 1):
    #         if ord(strr[i + 1]) == ord(strr[i]) + 1:
    #             cnt += 1
    #         else:
    #             break
    # else:
    #     cnt = 0

    ### ver2
    cnt = 0
    for i in range(len(strr)):
      if ord(strr[i]) == ord('a') + i:
        cnt += 1
      else:
        break

    print('#{} {}'.format(tc, cnt))