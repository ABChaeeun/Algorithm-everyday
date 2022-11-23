num = int(input())


lst = []
for i in range(num):
    age, name = input().split()
    age = int(age)
    lst.append([age, i, name]) # 가입 순서도 같이 넣어주기!!

# lst.sort()
lst = sorted(lst)    

for i in range(num):
    print(lst[i][0], lst[i][2])