answer, input_num = map(int, input().split())

cnt = 1
while answer != input_num:
    if answer != input_num:
        input_num += 1
        cnt += 1
        # print(answer, input_num)
        # print(cnt)g
    elif answer == input_num:
        # cnt += 1
        break

print(cnt)