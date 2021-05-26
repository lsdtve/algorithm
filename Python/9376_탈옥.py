import collections

dy = [0,0,1,-1]
dx = [1,-1,0,0]


def go(index, x, y):
    q = collections.deque()
    q.append([x, y])
    result[index][y][x] = min(result[index][y][x], 1 if graph[y][x] == "#" else 0)

    while q:
        x, y = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < H+2 and 0 <= nx < W+2:
                if graph[ny][nx] == "*":
                    continue

                temp = result[index][y][x]
                if graph[ny][nx] == "#":
                    temp += 1
                if result[index][ny][nx] > temp:
                    result[index][ny][nx] = temp
                    q.append([nx, ny])


for T in range(int(input())):
    H, W = map(int, input().split())
    graph = ["."*(W+2)]+["."+input()+"." for _ in range(H)]+["."*(W+2)]
    result = [[[99999999]*(W+2) for _ in range(H+2)] for _ in range(3)]

    cnt = 0
    for y in range(1, H+1):
        for x in range(1, W+1):
            if graph[y][x] == "$":
                go(cnt, x, y)
                cnt += 1
    go(2,0,0)

    ans = 9999999
    for y in range(H+2):
        for x in range(W+2):
            temp = result[0][y][x] + result[1][y][x] + result[2][y][x]
            if graph[y][x] == "#":
                temp -= 2
            ans = min(ans, temp)
    print(ans)