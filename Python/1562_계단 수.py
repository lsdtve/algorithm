N = int(input())
K = (1 << 10)
dp = [[[0]*(1 << 10) for _ in range(10)] for _ in range(N)]
mod = 1_000_000_000

for i in range(1, 10):
    dp[0][i][1 << i] = 1

for i in range(1, N):
    for j in range(10):
        for k in range(K):
            if j == 0:
                dp[i][j][k | (1<<j)] += dp[i-1][1][k]
            elif j == 9:
                dp[i][j][k | (1<<j)] += dp[i-1][8][k]
            else:
                dp[i][j][k | (1<<j)] += dp[i-1][j+1][k]
                dp[i][j][k | (1<<j)] += dp[i-1][j-1][k]
            dp[i][j][k | (1<<j)] %= mod
ans = 0
for i in range(10):
    ans += dp[N-1][i][K-1]
ans %= mod
print(ans)