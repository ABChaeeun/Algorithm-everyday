n = int(input())
s = []
dp = []
sum = 0

for i in range(n):
    s.append(int(input()))

dp.append(s[0])
dp.append(s[1])

for i in range (2, n):
    if ((s[-2] == dp[-1]) and (s[-3] == dp[-2])):
        dp.append( max( s[i], sum(dp) ) )
    else:
        dp.append(s[i])
print(dp)