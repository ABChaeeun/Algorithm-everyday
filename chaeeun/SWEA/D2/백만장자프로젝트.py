T = int(input())

for k in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    ### ceun - ver1
    # profit = 0
    # for i in range(len(lst)):
    #     lst2 = []
    #     for j in range(i, len(lst)):
    #         lst2.append(lst[j] - lst[i])
    #     profit += max(lst2)

    ### ceun - ver2
    profit = 0
    max_value = lst[-1]
    
    for i in range(N-2, -1, -1):
        if lst[i] >= max_value:
            max_value = lst[i]
        else:
            profit += max_value - lst[i]
        
    print("#%d %d" % (k, profit))
