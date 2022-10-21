T = int(input())

for tc in range(1, T+1):

    num = int(input())

    sum = 0
    for n in range(1, num+1):
        if n % 2 == 1: # 홀수 -> 더하기
            sum += n
        elif n % 2 == 0: # 짝수 -> 빼기
            sum -= n
            
    print('#{} {}'.format(tc, sum))