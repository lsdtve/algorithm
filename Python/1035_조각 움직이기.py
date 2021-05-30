import sys
sys.setrecursionlimit(10**6)
dy = [0,0,1,-1]
dx = [1,-1,0,0]


def go(cnt, distance):
    global ans

    if cnt == N:
        if connection_check():
            ans = min(ans, distance)
        return

    if distance >= ans:
        return

    for y in range(5):
        for x in range(5):
            if array[y][x] == ".":
                array[y][x] = '*'
                go(cnt + 1, distance + abs(piece[cnt][0]-y) + abs(piece[cnt][1]-x))
                array[y][x] = '.'
    return


def find_piece():
    for y in range(5):
        for x in range(5):
            if array[y][x] == '*':
                return [y, x]


def connection_check():
    y, x = find_piece()
    stack = [(y,x)]
    visited = {(y,x)}
    while stack:
        now = stack.pop()
        for d in range(4):
            ny = now[0] + dy[d]
            nx = now[1] + dx[d]
            if 0 <= ny < 5 and 0 <= nx < 5:
                if array[ny][nx] != "*":
                    continue
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    stack.append((ny, nx))
    if len(visited) == N:
        return True
    return False


array = [list(input()) for i in range(5)]
ans = 99999999
piece = []
for y in range(5):
    for x in range(5):
        if array[y][x] == "*":
            piece.append((y, x))
            array[y][x] = '.'
N = len(piece)
go(0, 0)
print(ans)