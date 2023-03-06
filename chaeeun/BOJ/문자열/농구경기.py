import sys
input = sys.stdin.readline

N = int(input())
lst = []
dictt = dict()
for i in range(N):
    lst.append(input())
    if lst[i][0] not in dictt:
        dictt[lst[i][0]] = 1
    else:
        dictt[lst[i][0]] += 1
    # print(lst[i][0], dictt[lst[i][0]])

cnt = 0
alph_lst = [] # 사전순 출력 위한.. 이거 안해서 틀렸었다...
for i, j in dictt.items():
    if j >= 5:
        alph_lst.append(i)
        cnt += 1

alph_lst.sort()
if cnt == 0:
    print('PREDAJA')
else:
    print(''.join(alph_lst))