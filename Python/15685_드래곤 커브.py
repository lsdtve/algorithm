dy = [0,-1,0,1]
dx = [1,0,-1,0]

N = int(input())
array = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    array[y][x] = 1
    curve = [d]
    for _ in range(g):
        temp = []
        for i in curve[::-1]:
            temp.append((i + 1) % 4)
        curve.extend(temp)

    for i in curve:
        y += dy[i]
        x += dx[i]
        array[y][x] = 1

ans = 0
for y in range(100):
    for x in range(100):
        if array[y][x] == 1 and array[y][x+1] == 1 and array[y+1][x] == 1 and array[y+1][x+1]:
            ans += 1
print(ans)
