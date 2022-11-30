num = input()

lst = []
for n in num:
    lst.append(int(n))


if len(lst) == 1 or len(lst) == 2:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")


else:
    cnt = 0
    for i in range(1, len(lst)-1):
        if (lst[i-1] - lst[i]) == (lst[i] - lst[i+1]): # 0보다 커야함
            cnt += 1
        else:
            print("흥칫뿡!! <(￣ ﹌ ￣)>") # 0이어야 함
            cnt = 0
            break
            
    if cnt > 0:
        print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
