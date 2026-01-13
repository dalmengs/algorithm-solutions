import heapq

INF = 9876543212345
n, m, k = map(int, input().split())

g = { i: [] for i in range(1, n + 1)}

for i in range(m):
    u, v, t = map(int, input().split())
    g[u].append([v, t])
    g[v].append([u, t])

dp = [[INF for _ in range(k + 1)] for _ in range(n + 1)]

q = []

heapq.heappush(q, (0, 1, 0))
dp[1][k] = 0

while len(q):
    now = heapq.heappop(q)

    now_cost = now[0]
    now_node = now[1]
    now_count = now[2]

    if dp[now_node][now_count] < now_cost:
        continue

    for nxt in g[now_node]:
        next_node = nxt[0]
        next_cost = nxt[1]

        # 다음 도로 포장
        if now_count < k:
            if dp[next_node][now_count + 1] == INF or now_cost < dp[next_node][now_count + 1]:
                dp[next_node][now_count + 1] = now_cost
                heapq.heappush(q, (now_cost, next_node, now_count + 1))

        # 다음 도로 포장하지 않음
        if dp[next_node][now_count] == INF or now_cost + next_cost < dp[next_node][now_count]:
            dp[next_node][now_count] = now_cost + next_cost
            heapq.heappush(q, (now_cost + next_cost, next_node, now_count))

print(min(dp[n]))