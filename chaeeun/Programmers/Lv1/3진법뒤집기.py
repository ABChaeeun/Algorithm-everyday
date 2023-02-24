def solution(n):
    
    ### 참고 전 풀이
    # three = convert(n, 3) ### convert() 함수 구현 참고 (10진법 -> n진법)
    # three_reverse = ''
    # for i in range(len(three)-1, -1, -1):
    #     three_reverse += three[i]
    
    ### 참고 후 풀이
    three_reverse = ''
    while n:
        three_reverse += str(n % 3)
        n = n // 3

    answer = int(three_reverse, 3)
    print(answer)
    
    return answer