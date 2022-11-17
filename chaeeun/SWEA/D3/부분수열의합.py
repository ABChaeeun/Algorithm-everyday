T = int(input())

def func(idx, sum):
    global answer

    if idx == N:
        return

    sum += lst[idx]

    if K == sum:
        answer += 1

    func(idx + 1, sum - lst[idx]) # 현재 인덱스 안 합하기
    func(idx + 1, sum) # 현재 인덱스 합하기

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    answer = 0
    func(0, 0)
    print('#{} {}'.format(tc, answer))