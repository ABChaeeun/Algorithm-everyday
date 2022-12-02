T = int(input())

for tc in range(1, T+1):
    str = input()
    
    for i in range(1, 12):
        if str[i] == str[0]:
            if str[0:i] in str:
                if str[i:i+i] in str[0:i]:
                    print('#{} {}'.format(tc, i))
                    break
