n, m = map(int, input().split())
heard = []
seen = []
heard_seen = []

for i in range(n):
    heard.append(input())
for j in range(m):
    seen.append(input())

for k in seen:
    if k in heard:
        heard_seen.append(k)

print(len(heard_seen))
print(sorted(heard_seen))