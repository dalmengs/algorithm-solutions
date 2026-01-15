from collections import deque

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
s = ["d", "l", "r", "u"]

def solve(n, m, x, y, r, c, K):
    q = deque()
    q.append([x, y, ""])

    while q:
        cx, cy, state = q.popleft()

        if K == len(state) and cx == r and cy == c:
            return state

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if len(state) + 1 > K: continue
            if nx <= 0 or nx > n or ny <= 0 or ny > m: continue

            remainCount = K - (len(state) + 1)
            remainDis = abs(r - nx) + abs(c - ny)

            if remainCount < remainDis: continue
            if (remainCount - remainDis) % 2 == 1: continue

            q.append([nx, ny, state + s[i]])
            break

    return "impossible"

def solution(n, m, x, y, r, c, k):
    answer = solve(n, m, x, y, r, c, k)
    return answer


print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))