import sys
sys.setrecursionlimit(123456)

n, m = map(int, input().split())

tree = [0 for i in range(n * 4)]
g = {i: [] for i in range(1, n + 1)}

e = [0] + list(map(int, input().split()))

for i in range(2, n + 1):
    g[i].append(e[i])
    g[e[i]].append(i)

def update_tree(start, end, idx, target, val):
    if target < start or target > end: return

    tree[idx] += val

    if start == end: return

    mid = (start + end) // 2
    update_tree(start, mid, idx * 2, target, val)
    update_tree(mid + 1, end, idx * 2 + 1, target, val)

def find_sum(start, end, idx, left, right):
    if right < start or end < left: return 0
    if left <= start and end <= right: return tree[idx]

    mid = (start + end) // 2
    return (
        find_sum(start, mid, idx * 2, left, right)
        + find_sum(mid + 1, end, idx * 2 + 1, left, right)
    )

cnt = 1
vis = [False for i in range(n + 1)]
dfn = [[0, 0] for i in range(n + 1)]
def dfs(now):
    global cnt
    vis[now] = True
    dfn[now][0] = cnt
    cnt += 1
    for nxt in g[now]:
        if vis[nxt]: continue
        dfs(nxt)
    dfn[now][1] = cnt - 1

dfs(1)

for _ in range(m):
    q = input().split()
    if q[0] == "1":
        i, w = map(int, q[1:])
        update_tree(1, n, 1, dfn[i][0], w)
    else:
        i = int(q[1])
        print(find_sum(1, n, 1, dfn[i][0], dfn[i][1]))