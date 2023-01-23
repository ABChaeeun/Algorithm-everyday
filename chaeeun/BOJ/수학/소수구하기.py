M, N = map(int, input().split())

def check_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1): # 루트 num
            if num % i == 0:
                return False
        return True

for i in range(M, N+1):
    if check_prime(i):
        print(i)