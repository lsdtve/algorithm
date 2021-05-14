from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
homes = []
chickens = []

ans = 99999999999

for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            homes.append([x, y])
        elif graph[y][x] == 2:
            chickens.append([x, y])

for chickens in combinations(chickens, M):
    result = 0
    for home in homes:
        temp = 999999999999
        for chicken in chickens:
            temp = min(temp, abs(home[0] - chicken[0]) + abs(home[1] - chicken[1]))
        result += temp
    ans = min(ans, result)
print(ans)