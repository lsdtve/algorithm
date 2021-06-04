def go(index):
    if dp[index] != -1:
        return dp[index]

    if not graph[index]:
        dp[index] = 0
        return 0

    temp = []
    for i in graph[index]:
        temp.append(go(i))
    temp.sort(reverse=True)

    for i in range(len(temp)):
        dp[index] = max(dp[index], temp[i] + i+1)
    return dp[index]


N = int(input())
array = list(map(int, input().split()))
dp = [-1]*N
graph = [[] for _ in range(N)]
start = 0
for i in range(N):
    if array[i] == -1:
        start = i
        continue
    graph[array[i]].append(i)
print(go(start))
