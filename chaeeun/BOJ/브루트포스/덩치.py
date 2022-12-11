num = int(input())

lst = []
for i in range(num):
    x, y = map(int, input().split())
    lst.append([x, y])

for i in range(num):  # lst 돌기
    # tmp = []
    rank = 1
    for j in range(num):  # lst에서 i 하나 잡고 다른것들이랑 비교
        if i != j:
            # print(i, j)
            # tmp.append([lst[i][0] - lst[j][0],
            #             lst[i][1] - lst[j][1]])
            if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]: #[ceun] 참고
                rank += 1

    # print(tmp)
    # print()
    print(rank, end=' ')
