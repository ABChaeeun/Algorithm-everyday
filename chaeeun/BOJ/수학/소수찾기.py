N = int(input())
lst = list(map(int, input().split()))


def check_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
cnt = 0
for i in range(len(lst)):
    if check_prime(lst[i]):
        cnt += 1

print(cnt)