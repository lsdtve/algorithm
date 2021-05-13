from collections import deque

def bfs(N):
    q = deque([N])
    dp[N] = 0
    while q:
        n = q.popleft()
        if n == K:
            return

        temp = 2*n
        while temp <= 100_000:
            if temp <= 0:
                break
            if dp[temp] < 0:
                q.append(temp)
                dp[temp] = dp[n]
            temp *= 2

        for i in [1, -1]:
            if not (0 <= n+i < 100_000):
                continue
            if dp[n+i] < 0:
                q.append(n + i)
                dp[n+i] = dp[n]+1

N, K = map(int, input().split())
dp = [-1] * 100_001
bfs(N)
print(dp[K])
