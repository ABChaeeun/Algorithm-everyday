# 많이 나온 수에 큰 숫자(9-)를 준다. (->X 자리수 큰거부터 줘야함)

import sys
input = sys.stdin.readline

n = int(input())
words = []
dic = dict()

for _ in range(n):
    words.append(input().rstrip())

for word in words:
    # 0의 개수 (자리수-1) 
    tmp = len(word) - 1
    for c in word:
        if c in dic:
            dic[c] += (10 ** tmp)
        else:
            dic[c] = (10 ** tmp)
        tmp -= 1 

# 자릿수 더한거 큰거부터 정렬
sorted_dic = sorted(dic.items(), key = lambda item: item[1], reverse = True)
k = 9
ans = 0
for s in sorted_dic:
    ans += s[1]*k
    k -= 1
print(ans)