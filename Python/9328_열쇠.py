dy = [0,0,-1,1]
dx = [1,-1,0,0]

def go(x, y):
    stack = [[x, y]]
    visited = [[False]*(W+2) for _ in range(H+2)]
    visited[y][x] = True
    while stack:
        x, y = stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < W+2 and 0 <= ny < H+2:
                if visited[ny][nx] or array[ny][nx] == "*":
                    continue
                if array[ny][nx] == "$":
                    global ans
                    array[ny][nx] = "."
                    ans += 1
                elif array[ny][nx].islower():
                    keys[ord(array[ny][nx]) - ord('a')] = True
                    array[ny][nx] = "."
                    visited = [[False] * (W + 2) for _ in range(H + 2)]
                elif array[ny][nx].isupper():
                    if not keys[ord(array[ny][nx]) - ord('A')]:
                        continue
                    array[ny][nx] = "."
                stack.append([nx, ny])
                visited[ny][nx] = True


for _ in range(int(input())):
    H, W = map(int, input().split())
    array = [list("."*(W+2))] + [list("."+input()+".") for _ in range(H)] + [list("."*(W+2))]
    keys = [False]*26
    ans = 0
    for key in input():
        if not key.isalpha():
            break
        keys[ord(key) - ord('a')] = True
    go(0, 0)
    print(ans)
