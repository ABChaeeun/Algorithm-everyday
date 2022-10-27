


num = int(input())

card = set(map(int,input().split()))

check = int(input())
check_card = list(map(int,input().split()))



for i in check_card:
    if i in card:
        print('1',end=' ')
    else :
        print('0',end=' ')
