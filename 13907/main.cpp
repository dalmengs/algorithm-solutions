#include <bits/stdc++.h>
using namespace std;

static const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, K;
    cin >> N >> M >> K;

    int S, D;
    cin >> S >> D;
    S--; D--;

    vector<vector<pair<int,int>>> graph(N);
    for (int i = 0; i < M; i++) {
        int u, v, c;
        cin >> u >> v >> c;
        u--; v--;
        graph[u].push_back({v, c});
        graph[v].push_back({u, c});
    }

    vector<vector<long long>> dist(N, vector<long long>(N + 1, INF));

    priority_queue<
        tuple<long long,int,int>,
        vector<tuple<long long,int,int>>,
        greater<tuple<long long,int,int>>
    > pq;

    dist[S][0] = 0;
    pq.push({0, S, 0});

    while (!pq.empty()) {
        auto [curDist, cur, cnt] = pq.top();
        pq.pop();

        if (cnt > N) continue;
        if (dist[cur][cnt] < curDist) continue;

        if (cnt == N) continue; // 더 늘릴 의미 없음

        for (auto &edge : graph[cur]) {
            int nxt = edge.first;
            int cost = edge.second;

            long long nd = curDist + cost;
            if (nd < dist[nxt][cnt + 1]) {
                dist[nxt][cnt + 1] = nd;
                pq.push({nd, nxt, cnt + 1});
            }
        }
    }

    long long taxSum = 0;

    for (int i = 0; i <= K; i++) {
        long long tax;
        if (i == 0) tax = 0;
        else cin >> tax;

        taxSum += tax;

        long long ans = INF;
        for (int e = 0; e <= N; e++) {
            if (dist[D][e] == INF) continue;
            ans = min(ans, dist[D][e] + taxSum * e);
        }

        cout << ans << '\n';
    }

    return 0;
}
