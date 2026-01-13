n, m, k = map(int, input().split())

MAX = 1_000_000_000

dp = [[-1] * (m + 1) for _ in range(n + 1)]

def cnt(n, m):
    if n == 0 or m == 0:
        return 1
    if dp[n][m] != -1:
        return dp[n][m]

    dp[n][m] = min(MAX, cnt(n - 1, m) + cnt(n, m - 1))
    return dp[n][m]

def dfs(n, m, k):
    if n == 0:
        return "z" * m
    if m == 0:
        return "a" * n

    first_a = cnt(n - 1, m)

    if k <= first_a:
        return "a" + dfs(n - 1, m, k)
    else:
        return "z" + dfs(n, m - 1, k - first_a)


if cnt(n, m) < k:
    print(-1)
else:
    print(dfs(n, m, k))
