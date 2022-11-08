n, m = map(int, input().split())
heard = set()
seen = set()

for i in range(n):
    heard.add(input())

for j in range(m):
    seen.add(input())

heard_seen = sorted(list(heard & seen))

print(len(heard_seen))
for l in heard_seen:
    print(l)