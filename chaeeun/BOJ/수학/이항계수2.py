import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def f(a, b, answer):
    for i in range(a-b):
        answer *= a
        a -= 1
    return answer

def factorial(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer
        
result = f(n, n-k, 1) // factorial(k)
print(result % 10007)