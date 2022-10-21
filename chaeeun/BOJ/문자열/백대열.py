n, m = map(int, input().split(':'))


# 최대공약수 찾기
def GCD(a, b):
    min_num = min(a, b)
    for i in range(min_num, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


gcd_num = GCD(n, m)
n_result = n // gcd_num
m_result = m // gcd_num

print('{}:{}'.format(n_result, m_result))