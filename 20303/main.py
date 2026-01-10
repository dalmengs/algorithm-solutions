import sys
sys.setrecursionlimit(10**5 + 100)

t = int(input())

def solve():
    n = int(input())
    v = list(map(int, input().split()))

    g = { i : [] for i in range(1, n + 1)}
    for i in range(n):
        g[i + 1].append(v[i])

    team = [0 for _ in range(n + 1)]
    vis = [0 for _ in range(n + 1)]
    cycle_found = [0]

    def dfs(now, id):
        vis[now] = id

        for nxt in g[now]:
            if vis[nxt] == 0:
                dfs(nxt, id)
            elif vis[nxt] == id:
                cycle_found[0] = nxt

        if cycle_found[0] != 0:
            team[now] = cycle_found[0]
        if now == cycle_found[0]:
            cycle_found[0] = 0

    for i in range(1, n + 1):
        cycle_found[0] = 0
        if vis[i] == 0: dfs(i, i)

    print(team.count(0) - 1)

for _ in range(t):
    solve()