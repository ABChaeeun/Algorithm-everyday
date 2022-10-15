def solution(sizes):
    answer = 0
    x_max=0
    y_max=0
    sizesarr=[]
    for i in range(0,len(sizes)):
        sizes[i].sort()
        x_max = max(x_max,sizes[i][0])
        y_max = max(y_max,sizes[i][1])
    return x_max*y_max

sizes = [[60,50],[30,70],[60,30],[80,40]]

print(solution(sizes))