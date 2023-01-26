# 참고 - 문제이해..

A, B = map(int, input().split())

def GCD(a, b):
    while b > 0:
        a, b = b, a%b
    return a
    
print('1'*GCD(A, B)) # 최대공약수의 값만큼 1을 출력