dp = [99999]*100
dp[0] = 0
coin = [1, 10, 25]
for i in range(100):
    for c in coin:
        if i+c >= 100:
            continue
        dp[i+c] = min(dp[i+c], dp[i]+1)


for _ in range(int(input())):
    N = int(input())
    ans = 0
    while N:
        ans += dp[N % 100]
        N = N // 100
    print(ans)
