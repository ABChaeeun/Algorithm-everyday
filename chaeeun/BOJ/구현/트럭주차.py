# 참고 - 아이디어(입력으로 주어지는 시간의 최대 숫자가 100이니까 result배열 만들어놓고 값 써놓으면 되는..!)
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

result = [0]*100
for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        result[i] += 1
# print(result)

answer = 0
for i in range(len(result)):
    if result[i] == 1:
        answer += A
    elif result[i] == 2:
        answer += B*2
    elif result[i] == 3:
        answer += C*3

print(answer)