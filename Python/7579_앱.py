N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
cost_tot = sum(cost)
dp = [0] * (cost_tot + 1)

for i in range(N):
    for c in range(cost_tot, cost[i]-1, -1):
        dp[c] = max(dp[c], dp[c - cost[i]] + memory[i])
for i in range(cost_tot+1):
    if dp[i] >= M:
        print(i)
        break