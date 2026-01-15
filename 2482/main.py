INF = int(1e9)

def check(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt

def solve():
    x = " " + input()
    y = " " + input()

    n = len(x) - 1

    dp = [[[INF, INF], [INF, INF]]] * (n + 1)

    if x[1] == "0":
        if y[1] == "1":
            dp[1][1][1] = 1
    else:
        if y[1] == "1":
            dp[1][0][0] = 1

    for i in range(2, n + 1):
        c = x[i] + y[i]

        dp[i][0][0] = min(
            dp[i][0][0],
            dp[i - 1][0][0] + check("00", c),
            dp[i - 1][1][0] + check("00", c),
        )
        dp[i][0][1] = min(
            dp[i][0][1],
            dp[i - 1][0][1] + check("00", c),
            dp[i - 1][1][1] + check("00", c),
        )
        dp[i][1][0] = min(
            dp[i][1][0],
            dp[i - 1][0][1] + check("00", c),
            dp[i - 1][1][1] + check("00", c),
        )
        dp[i][1][1] = min(
            dp[i][1][1],
            dp[i - 1][0][0] + check("00", c),
            dp[i - 1][1][0] + check("00", c),
        )

    print(min(dp[n][0] + dp[n][1]))






t = int(input())
for _ in range(t):
    solve()