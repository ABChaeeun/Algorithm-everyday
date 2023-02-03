n = int(input())
nlst = list(map(int, input().split()))
m = int(input())
mlst = list(map(int, input().split()))

dictt = {}
for i in nlst:
    dictt[i] = 0

for i in range(m):
    if mlst[i] in dictt:
        print(1, end = ' ')
    else:
        print(0, end = ' ')