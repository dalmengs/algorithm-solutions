import sys
sys.setrecursionlimit(123456)

k = int(input())
n = 2 ** (k + 1) - 1

w = list(map(int, input().split()))

g = { i: [] for i in range(1, n + 1) }
for i in range(len(w)):
    src = (i + 2) // 2
    dest = i + 2

    g[src].append([dest, w[i], w[i]])

vis = [0 for i in range(n + 1)]

def dfs(now):
    vis[now] = 1

    ret = 0
    ws = []
    for nxt in g[now]:
        node_idx = nxt[0]
        node_weight = nxt[1]

        if vis[node_idx]: continue
        res = dfs(node_idx)
        ws.append(res[0] + node_weight)
        ret += res[1]

    if len(ws) == 0:
        return [0, 0]

    m = max(ws)
    q = 0

    idx = -1
    for nxt in g[now]:
        idx += 1
        q += m - ws[idx]
        g[now][idx][2] += m - ws[idx]

    return [m, ret + q]

dfs(1)

vis = [0 for i in range(n + 1)]
def ans(now):
    vis[now] = 1
    ret = 0
    for nxt in g[now]:
        node_idx = nxt[0]
        node_weight = nxt[2]
        if vis[node_idx]: continue
        ret += (ans(node_idx) + node_weight)
    return ret

print(ans(1))