import sys
input = sys.stdin.readline


pado = [0,1,1,1,2,2,]

def padoban(N):
    for i in range(6,101):
        pado.append(pado[i-1]+pado[i-5])


T = int(input())
for _ in range(T):
    N = int(input())
    padoban(N)
    print(pado[N])