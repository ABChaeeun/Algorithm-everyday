for _ in range(10):
    tc = int(input())
    N, M = map(int, input().split())
    
    def recur(n, m):
        if m == 1:
            return n
        else:
            return n * recur(n, m-1)
    
    
    print('#{} '.format(tc), end='')
    print(recur(N, M))