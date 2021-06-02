INF = 99999999

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
power = sum([1 << index if value == "Y" else 0 for index,value in enumerate(input())])
P = int(input())
dp = [INF] * (1 << N)
dp[power] = 0
for i in range(1 << N):
    if dp[i] == INF:
        continue
    for j in range(N):
        if i & (1 << j):
            for n in range(N):
                if (i & (1 << n)) == 0:
                    dp[i | (1 << n)] = min(dp[i | (1 << n)], dp[i] + graph[j][n])

ans = INF
for i in range(1 << N):
    if dp[i] == INF:
        continue
    cnt = 0
    for j in range(N):
        if i & (1 << j):
            cnt += 1
    if cnt >= P:
        ans = min(ans, dp[i])

print(-1 if ans == INF else ans)
