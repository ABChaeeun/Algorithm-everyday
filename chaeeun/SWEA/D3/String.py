for _ in range(10):
    tc = int(input())
    find = input()
    ori = input()

    answer = 0
    for i in range(len(ori)-len(find)+1): # +1 해줘야 !!
        if ori[i] == find[0]:
            tmp = 0
            for j in range(len(find)):
                if ori[i+j] == find[j]:
                    tmp += 1
                else:
                    break # tmp = 0 으로 해주면 안됨!
            if tmp == len(find): # find가 ori에 있을 때 다 더해준 값이 find의 길이와 같을 경우
                answer += 1

    print('#{} {}'.format(tc, answer))
