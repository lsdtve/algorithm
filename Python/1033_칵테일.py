from math import gcd


def dfs(node):
    stack = [node]
    visited = [False] * N
    visited[node] = True
    while stack:
        now = stack.pop()
        for i in graph[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                stack.append(i[0])
                result[i[0]] = result[now] * i[2] // i[1]

N = int(input())
graph = [[] for _ in range(N)]
result = [0]*N
lcm = 1
for i in range(N-1):
    a,b,p,q = map(int, input().split())
    graph[a].append([b,p,q])
    graph[b].append([a,q,p])
    lcm *= (p*q)//gcd(p,q)


result[1] = lcm
dfs(1)

result_gcd = result[0]
for i in result:
    result_gcd = gcd(result_gcd, i)
for i in range(N):
    result[i] //= result_gcd
print(*result)
