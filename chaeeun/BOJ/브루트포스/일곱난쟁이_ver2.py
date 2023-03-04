lst = []
for _ in range(9):
    lst.append(int(input()))

a = 0
b = 0
lst.sort()
over = sum(lst) - 100
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == over:
            a = lst[i]
            b = lst[j]
            break

### 이렇게 하지 말고 a, b로 해주니 맞음
# for atom in over_lst:
#     del lst[lst.index(atom)]

for atom in lst:
    if not (atom == a or atom == b):
        print(atom)