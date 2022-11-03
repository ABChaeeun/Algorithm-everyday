import sys
input = sys.stdin.readline

def binary_search(start, end, data):
    result = 0
    while start <= end:
        mid = (start+end)// 2
        length = 0 
        for tree in data:
            if tree >= mid:
                length += (tree-mid)
            else :
                continue
        if length >= M:
            start = mid + 1
            result = mid
        else :
            end = mid -1
    return result

N , M = map(int,input().split())
data = list(map(int,input().split()))
start = 1
end = max(data)
print(binary_search(start,end,data))