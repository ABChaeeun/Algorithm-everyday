N, M = map(int, input().split())

def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def LCM(a, b):
    return int(a * b / GCD(N, M))

print(GCD(N, M))
print(LCM(N, M))