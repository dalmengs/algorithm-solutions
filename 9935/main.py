s1 = input()
s2 = input()

q = []

for s in s1:
    q.append(s)

    if len(q) < len(s2):
        continue

    ts = q[len(q)-len(s2):]
    if "".join(ts) == s2:
        for _ in range(len(s2)):
            q.pop()

if not q:
    print("FRULA")
else:
    print("".join(q))