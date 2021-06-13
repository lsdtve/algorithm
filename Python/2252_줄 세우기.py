import collections

N, M = map(int, input().split())
inDegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    inDegree[b] += 1
    graph[a].append(b)

q = collections.deque()
for i in range(1, N+1):
    if inDegree[i] == 0:
        q.append(i)

for i in range(1, N+1):
    if not q:
        break
    now = q.popleft()
    for j in graph[now]:
        inDegree[j] -= 1
        if inDegree[j] == 0:
            q.append(j)
    print(now, end=" ")