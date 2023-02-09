def solution(triangle):
    d = triangle.copy()
    for i in range(1, len(d)):
        for j in range(0, len(d[i])):
            if j-1 < 0:
                d[i][j] += d[i-1][j]
            elif j >= len(d[i-1]):
                d[i][j] += d[i-1][j-1]
            else:
                d[i][j] += max(d[i-1][j], d[i-1][j-1])
    return max(d[len(triangle)-1])