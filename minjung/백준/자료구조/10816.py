from collections import Counter

num = int(input())
card = list(map(int,input().split()))
check = int(input())
check_card = list(map(int,input().split()))
res = [0]*check

count = Counter(card)
for i in range(len(check_card)):
    if check_card[i] in count:
        print(count[check_card[i]],end=' ')
    else:
        print('0',end=' ')