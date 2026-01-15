n = int(input())
p = list(map(int, input().split()))
m = int(input())

def cmp(x, y):
    if len(x) != len(y):
        if len(x) > len(y):
            return x
        return y
    return x if x > y else y

dp = [["" for _ in range(51)] for _ in range(51)]

def dfs(balance, digit):

    if balance == 0: return ""
    if dp[balance][digit] != "": return str(dp[balance][digit])

    ret = ""
    for i in range(n):
        if digit == 0 and i == 0: continue
        if balance - p[i] < 0: continue

        res = f"{i}" + dfs(balance - p[i], digit + 1)

        if ret == "" or cmp(ret, res) == res:
            ret = res

    if ret != -1:
        dp[balance][digit] = ret
    return ret


ans = dfs(m, 0)
print(ans if len(ans) else 0)
