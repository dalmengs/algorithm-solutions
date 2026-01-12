import sys
sys.setrecursionlimit(10**5 + 100)

n, m, k = map(int, input().split())
c = [0] + list(map(int, input().split()))

g = { i: [] for i in range(n + 1) }

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

vis = [0 for _ in range(n + 1)]

def dfs(now, id):
    vis[now] = id

    for nxt in g[now]:
        if vis[nxt]: continue
        dfs(nxt, id)

for i in range(1, n + 1):
    if vis[i]: continue
    dfs(i, i)

group = {}
for i in range(1, n + 1):
    group_id = vis[i]
    if group_id not in group:
        group[group_id] = [0, 0]
    curr = group[group_id]
    group[group_id] = [curr[0] + 1, curr[1] + c[i]]

data = [group[i] for i in group]
dp = [0 for _ in range(k)]

for i in group:
    cap, cnt = group[i]
    for p in range(k - 1, cap - 1, -1):
        dp[p] = max(dp[p], dp[p - cap] + cnt)

print(max(dp))