def go(target, cnt, value):
    global ans
    ans = max(ans, cnt)
    for i in range(N):
        if target == i:
            continue
        if not visited[i] and value <= graph[target][i]:
            visited[i] = True
            go(i, cnt+1, graph[target][i])
            visited[i] = False


N = int(input())
graph = [list(map(int, list(input()))) for _ in range(N)]
print(graph)
ans = 1
visited = [False] * N
go(0, 1, 0)
print(ans)
