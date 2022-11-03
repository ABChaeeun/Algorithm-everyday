N = int(input())

num = 0
i = 0
while(1):
    num += 1
    if '666' in str(num):
        i += 1
        if i == N:
            print(num)
            break