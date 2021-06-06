import heapq
import sys
read = sys.stdin.readline
INF = 9999999999

N = int(input())
q = []
for i in range(N):
    heapq.heappush(q,(int(read()),i))
graph = [list(map(int, read().split())) for _ in range(N)]

node = [INF] * N
while len(q) > 0:
    cost, index = heapq.heappop(q)

    if node[index] != INF:
        continue

    node[index] = cost

    for i in range(N):
        if node[i] != INF:
            continue
        heapq.heappush(q,(graph[index][i],i))
print(sum(node))