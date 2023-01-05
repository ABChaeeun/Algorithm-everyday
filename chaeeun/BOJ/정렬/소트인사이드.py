N = input()

lst = []
for i in N:
    lst.append(int(i))

lst.sort(reverse = True)

for i in range(len(lst)):
    print(lst[i], end='')