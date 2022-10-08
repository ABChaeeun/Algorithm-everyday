num = int(input())

for i in range(1, num+1):
    quotient = 0
    remainder = 0
    a, b = map(int, input().split())
    quotient = int(a/b)
    remainder = int(a%b)
    print("#%d %d %d" %(i, quotient, remainder))