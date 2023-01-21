import sys
input = sys.stdin.readline

s = input().strip()

def recursive(x):
    if len(x) == 1:
        return True
    else:
        return x == x[::-1] and recursive(x[:len(x)//2]) # [::--1] : 거꾸로 뒤집은 string이 원본과 같은지 and 재귀
    
if recursive(s):
    print("AKARAKA")
else:
    print("IPSELENTI")