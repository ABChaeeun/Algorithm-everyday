import sys
input = sys.stdin.readline

def binary_search(start,end,data):
    result = 0
    while start <= end:
        mid = (start + end) //2
        total = 0
        for lan in data :
            total += lan // mid
        if total >= N :
            start = mid + 1
            result = mid
        else :
            end = mid - 1
    return result
K , N = map(int,input().split())

data=[int(input()) for _ in range(K)]
start = 1
end = max(data)
print(binary_search(start,end,data))


