num = int(input())

result = 0
while num > 0:
    if num % 5 == 0:
        result += num // 5
        num = 0
        break
    else:
        num -= 3
        result += 1

if num:
    print(-1)
else:
    print(result)
