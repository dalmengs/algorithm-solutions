n, p, q = map(int, input().split())

dp = { 0: 1}

def dfs(now):
    if now == 0: return 1

    if now in dp:
        return dp[now]

    dp[now] = dfs(now // p) + dfs(now // q)
    return dp[now]

print(dfs(n))