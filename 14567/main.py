from collections import deque

n, m = map(int, input().split())

g = { i: [] for i in range(1, n + 1) }
indegree = [0 for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    indegree[v] += 1

q = deque()

sem = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append([i, 1])
        sem[i] = 1

while q:
    now, se = q.popleft()

    for next in g[now]:
        indegree[next] -= 1
        sem[next] = se + 1
        if indegree[next] == 0:
            q.append([next, se + 1])

print(" ".join(list(map(str, sem[1:]))))