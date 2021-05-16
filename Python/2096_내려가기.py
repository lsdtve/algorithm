import sys
read = sys.stdin.readline

N = int(input())
graph = list(map(int, read().split()))
maxDp = [graph.copy()] + [[0,0,0]]
minDp = [graph.copy()] + [[0,0,0]]
for t in range(1, N):
    i = t % 2
    graph = list(map(int, read().split()))
    maxDp[i][0] = max(maxDp[i-1][:2]) + graph[0]
    maxDp[i][1] = max(maxDp[i-1]) + graph[1]
    maxDp[i][2] = max(maxDp[i-1][1:]) + graph[2]

    minDp[i][0] = min(minDp[i-1][:2]) + graph[0]
    minDp[i][1] = min(minDp[i-1]) + graph[1]
    minDp[i][2] = min(minDp[i-1][1:]) + graph[2]

print(max(maxDp[(N % 2) -1]), min(minDp[(N % 2) -1]))