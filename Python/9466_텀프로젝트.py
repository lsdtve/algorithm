import sys
read = sys.stdin.readline
sys.setrecursionlimit(99999999)

def dfs(start):
    visited[start] = True
    cycle.append(start)
    next = array[start]

    if visited[next]:
        if next in cycle:
            global ans
            ans -= len(cycle) - cycle.index(next)
        return
    else:
        dfs(next)

T = int(read())
for _ in range(T):
    n = int(read())
    array = [0] + list(map(int, read().split()))
    visited = [True] + [False] * n
    ans = n
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(ans)
