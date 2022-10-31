import sys
input = sys.stdin.readline

def binary_search(data):
    start = 1
    end = max(data)
    total = 0
    while start <= end:
        mid = (start + end) //2
        for lan in data :
            total += lan // mid
        if total >= N :
            start = mid + 1
            return mid
        else :
            end = mid - 1

K , N = map(int,input().split())

data = []
for i in range(K):
    data.append(int(input()))

print(binary_search(data))
