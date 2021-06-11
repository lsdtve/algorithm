N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

for x in range(M):
    dp[0][x] = dp[0][x-1] + graph[0][x]

for y in range(1, N):
    left = [dp[y-1][x] + graph[y][x] for x in range(M)]
    right = [dp[y-1][x] + graph[y][x] for x in range(M)]
    for x in range(M-1):
        right[x+1] = max(right[x+1], right[x] + graph[y][x+1]) + graph
    for x in range(M-1, 0, -1):
        left[x-1] = max(left[x-1], left[x] + graph[y][x-1])
    for x in range(M):
        dp[y][x] = max(left[x], right[x])
print(dp[N-1][M-1])
