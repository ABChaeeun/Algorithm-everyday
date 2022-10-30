import sys
input = sys.stdin.readline

def binary_search(target, data):
    start = 0
    end = N- 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
           
        else :
            end = mid - 1
    return None

N = int(input())
A = list(map(int,input().split()))
M = int(input())
num = list(map(int,input().split()))
A.sort()
for i in num:
    idx = binary_search(i,A)
    if idx != None:
        print(1)
    else :
        print(0)