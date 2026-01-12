import sys
sys.setrecursionlimit(150000)

n = int(input())

t = ['S' for _ in range(n + 1)]
c = [0 for _ in range(n + 1)]
g = { i: [] for i in range(1, n + 1)}

for i in range(2, n + 1):
    ty, count, nxt = input().split()
    t[i] = ty
    c[i] = int(count)

    nxt = int(nxt)
    g[i].append(nxt)
    g[nxt].append(i)

vis = [False for _ in range(n + 1)]

def dfs(now):
    vis[now] = True

    ret = 0
    is_leaf = True
    for nxt in g[now]:
        if vis[nxt]: continue
        is_leaf = False
        ret += dfs(nxt)

    ret = max(ret - (c[now] if t[now] == 'W' else -c[now]), 0)
    if is_leaf:
        ret = c[now] if t[now] == 'S' else 0

    return ret

print(dfs(1))