K = int(input())
dp = []

for i in range(K+1):
    if len(dp) == 0:
        dp.append(0)
    elif len(dp) == 1:
        dp.append(1)
    else:
        dp.append(dp[-1] + dp[-2])

print(dp[-2], dp[-1])

### A -> B
### B -> BA
# A
# B                     # 0 1 # 1
# BA                    # 1 1 # 2
# BA B                  # 1 2 # 3
# BA B BA               # 2 3 # 4
# BA B BA BA B          # 3 5 # 5
# BA B BA BA B BA B BA  # 5 8 # 6

### idea : 피보나치 수열!!