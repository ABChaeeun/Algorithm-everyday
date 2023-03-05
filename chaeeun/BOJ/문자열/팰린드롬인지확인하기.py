strr = input()

cnt = 0

if len(strr) % 2 == 1:  # 문자열의 길이가 홀수
    for i in range(1, len(strr) // 2 + 1):
        if strr[len(strr) // 2 + i] == strr[len(strr) // 2 - i]:
            cnt += 1
        else:
            cnt = -1
            break
else:  # 문자열의 길이가 짝수
    for i in range(0, len(strr) // 2):
        if strr[int((len(strr) - 1) / 2 + i +
                    0.5)] == strr[int((len(strr) - 1) / 2 - i - 0.5)]:
            cnt += 1
        else:
            cnt = -1
            break

### 여기서 틀려서 고침!!
if cnt == -1:
    print(0)
else:
    print(1)
