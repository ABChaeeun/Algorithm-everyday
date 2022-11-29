# 파이썬은 소수점 15자리까지만 표시

A, B, N = map(int, input().split())

### idea: 초등학교때 배운 몫과 나머지 계산하는 방법. 수학적으로 접근
for i in range(N):
    A = (A%B)*10
    result = A//B
        
print(result)
