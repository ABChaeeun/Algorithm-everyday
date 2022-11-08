# print(ord('z'))
# print(ord('{'))
# print(ord('}'))
T = int(input())

for tc in range(1, T + 1):
    strr = input()

    ### ver1
    # cnt = 1
    # if strr[0] == 'a':
    #     for i in range(0, len(strr) - 1):
    #         if ord(strr[i + 1]) == ord(strr[i]) + 1:
    #             cnt += 1
    #         else:
    #             break
    # else:
    #     cnt = 0

    ### ver2
    cnt = 0
    for i in range(len(strr)):
      if ord(strr[i]) == ord('a') + i:
        cnt += 1
      else:
        break

    print('#{} {}'.format(tc, cnt))

# # print(ord('A'))
# # print(ord('A')+1)
#######################################
# T = int(input())
# for tc in range(1, T + 1):
#     strr = input()
#     cnt = 0
#     for i in range(0, len(strr)):
#       if ord(strr[i]) == ord('a') + i:
#         cnt += 1
#       else:
#         break
#     print('#{} {}'.format(tc, cnt))

