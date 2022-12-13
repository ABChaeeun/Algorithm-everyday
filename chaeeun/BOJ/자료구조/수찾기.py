N = int(input())
A = set(map(int, input().split())) ### 이전풀이 : list
M = int(input())
M_list = list(map(int, input().split()))

for m in M_list:
    if m in A:
        print('1')
    else:
        print('0')
