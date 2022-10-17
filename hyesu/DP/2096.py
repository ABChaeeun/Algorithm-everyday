import sys
input = sys.stdin.readline

n = int(input())

maxdp = [0, 0, 0]
mindp = [0, 0, 0]

score = []

for _ in range(n):
    a, b, c = map(int, input().split())
    score.append((a, b, c))

for i in range(n):
    tmpMax = [0, 0, 0]
    tmpMin = [0, 0, 0]
    for j in range(3):
        if j == 0:
            tmpMax[j] = max(maxdp[0], maxdp[1]) + score[i][j]
            tmpMin[j] = min(mindp[0], mindp[1]) + score[i][j]
        elif j == 2:
            tmpMax[j] = max(maxdp[1], maxdp[2]) + score[i][j]
            tmpMin[j] = min(mindp[1], mindp[2]) + score[i][j]
        else:
            tmpMax[j] = max(maxdp) + score[i][j]
            tmpMin[j] = min(mindp) + score[i][j]
    maxdp = tmpMax
    mindp = tmpMin
        
print(max(maxdp), min(mindp))