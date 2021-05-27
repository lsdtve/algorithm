import sys
sys.setrecursionlimit(10**6)

def dfs(start):
    for i in range(graph[start][0], graph[start][1] + 1):
        if visited[i]:
            continue
        visited[i] = True
        if d[i] == -1 or dfs(d[i]):
            d[i] = start
            return True
    return False


T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    visited = [False] * (N + 1)
    d = [-1] * (N + 1)
    graph = [list(map(int, input().split())) for _ in range(M)]
    for j in range(M):
        visited = [False] * (N + 1)
        dfs(j)
    ans = 0
    for s in d:
        if s != -1:
            ans += 1
    print(ans)