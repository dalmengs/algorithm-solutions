s = []
for i in input():
    s.append(i)

c = None
q = []

for i in range(len(s)):
    q.append(s[i])

    if s[i] == ")" or s[i] == "]":
        c = s[i]

    if not c: continue

    m = None

    if len(q) - 2 < 0: continue

    for j in range(len(q) - 2, -1, -1):
        if q[j] not in "()[]": continue

        if (c == ")" and q[j] != "(") or (c == "]" and q[j] != "["):
            print(0)
            exit()

        p = q[j:]
        for _ in range(len(p)):
            q.pop()

        val = 0
        if len(p) == 2:
            if p[0] == "(":
                val = 2
            else:
                val = 3
        else:
            for k in p[1:-1]:
                val += int(k)
            if p[0] == "(":
                val *= 2
            else:
                val *= 3

        q.append(str(val))

        c = None
        break

ans = 0
for v in q:
    if v in "()[]":
        print(0)
        exit()

    ans += int(v)

print(ans)