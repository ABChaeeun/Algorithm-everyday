# 조합 (combination) 이용

import itertools

N, S = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
for count in range(1, N+1):
    nCr = itertools.combinations(lst, count)
    # print(list(nCr))
    for num in nCr:
        if sum(num) == S:
            cnt += 1

print(cnt)