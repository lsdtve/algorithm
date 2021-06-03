import collections
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(height, x, y):
    q = collections.deque()
    q.append((x, y))
    visited = [[False]*M for _ in range(N)]
    visited[y][x] = True

    result = [[x, y]]
    while q:
        x, y = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if array[ny][nx] < height and not visited[ny][nx] and not ans_visited[ny][nx]:
                    q.append((nx, ny))
                    visited[ny][nx] = True
                    result.append([nx, ny])
            else:
                return
    for x, y in result:
        global ans
        ans += height - array[y][x]
        ans_visited[y][x] = True


N, M = map(int, input().split())
array = [list(map(int, input())) for _ in range(N)]
max_height = max(map(max, array))
ans = 0
ans_visited = [[False]*M for _ in range(N)]
for i in range(max_height, 0, -1):
    for y in range(N):
        for x in range(M):
            if array[y][x] < i and not ans_visited[y][x]:
                bfs(i, x, y)
print(ans)