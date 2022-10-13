T = int(input())
 
for k in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
 
    profit = 0
    for i in range(len(lst)):
        lst2 = []
        for j in range(i, len(lst)):
            lst2.append(lst[j] - lst[i])
        profit += max(lst2)
 
    print("#%d %d" % (k, profit))