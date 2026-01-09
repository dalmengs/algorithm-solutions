n = int(input())
h = []
for _ in range(n):
    h.append(int(input()))

cnt = 0

if n == 1:
    print(0)
    exit()

s = [h[0]]

for i in range(1, n):
    c = h[i]

    while len(s) > 0 and s[-1] <= c:
        s.pop()

    cnt += len(s)
    s.append(c)

print(cnt)