import math

while True:
    num = input()
    count = 0
    if num == '0':
        break
    else:
        for i in range(math.ceil(len(num))):
            if int(num) % 2 == 0:
                if num[i] != num[-(i+1)]:
                    print("no")
                    count += 1
                    break
            elif int(num) % 2 == 1:
                if num[i] != num[-(i+1)]:
                    print("no")
                    count += 1
                    break
        if count == 0:
            print("yes")


