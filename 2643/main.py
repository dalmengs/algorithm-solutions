import sys
sys.setrecursionlimit(10**5)

n = int(input())
s = []
for i in range(n):
    x, y = map(int, input().split())
    s.append([max(x, y), min(x, y)])

s = sorted(s, key=lambda x: (-x[0], -x[1]))

dp = [0 for _ in range(n + 1)]

def dfs(idx):
    if dp[idx] != 0: return dp[idx]

    ret = 0
    f = False
    for i in range(idx + 1, n):
        x, y = s[i]
        if x <= s[idx][0] and y <= s[idx][1]:
            f = True
            ret = max(ret, dfs(i) + 1)

    if not f: return 1

    dp[idx] = ret
    return ret

ans = 0
for i in range(n):
    ans = max(ans, dfs(i))

print(ans)