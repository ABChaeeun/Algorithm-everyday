import sys
input = sys.stdin.readline

def binary_search(start,end):
    result = 0
    while start <= end:
        mid = (start+end)//2
        length = 0
        cnt = 1
        prev_home = home[0]
        for i in range(N):
            if home[i] - prev_home >= mid:
                cnt+=1
                prev_home = home[i]
        if cnt >= C:
            result= max(result,mid)
            start = mid+1
        else:
            end = mid -1
    return result


N, C = map(int,input().split())
home = [int(input()) for _ in range(N)]

home.sort()
start = 1
end = home[N-1] - home[0]
print(binary_search(start,end))