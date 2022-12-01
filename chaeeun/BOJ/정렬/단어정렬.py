### input
N = int(input())
lst = []
for i in range(N):
    strr = input()
    lst.append([strr, len(strr)])

### 중복 제거 - set() 이용
sett = set(list(map(tuple, lst)))
new_lst = list(map(list, sett))

### 사전순 정렬
new_lst.sort()

### 길이순 정렬
new_lst.sort(key=lambda x:x[1])

### output
for i in range(len(new_lst)):
    print(new_lst[i][0])
