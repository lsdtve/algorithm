import sys
INF = sys.maxsize

def go(node, visited):
    if visited == (2**N - 1):
        if graph[node][0] == 0:
            return INF
        return graph[node][0]

    if dp[node][visited] != INF:
        return dp[node][visited]

    for i in range(N):
        if graph[node][i] == 0 or (visited & (1 << i)) != 0:
            continue
        next = visited | (1 << i)
        dp[node][visited] = min(dp[node][visited], go(i, next) + graph[node][i])

    return dp[node][visited]


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[INF]*(2**N - 1) for _ in range(N)]
print(go(0, 1))