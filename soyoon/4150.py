# 1. 재귀 구조 브루트 포스

# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

# print(fib(int(input())))

# 2. 메모이제이션(하향식)

# def fib(n):
#     dp = [0 for i in range(n+1)] 
#     if n <= 1:
#         return n
#     if dp[n] > 0:
#         return dp[n]
#     dp[n] = fib(n-1) + fib(n-2)
#     return dp[n]

# print(fib(int(input())))
# 3. 타뷸레이션(상향식)
def fib(n):
    dp = [0 for i in range(n+1)] 
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(fib(int(input())))