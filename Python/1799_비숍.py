def go(x, y, cnt, flag):
    global ans
    if x >= N:
        y += 1
        x = 0 if x % 2 else 1
    if y >= N:
        ans[flag] = max(ans[flag], cnt)
        return
    if array[y][x] == 1 and not R[x+y] and not L[y-x+N-1]:
        L[y-x+N-1], R[x+y] = True, True
        go(x+2, y, cnt + 1, flag)
        L[y-x+N-1], R[x+y] = False, False
    go(x+2, y, cnt, flag)


N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
R = [False]*(2*N)
L = [False]*(2*N)
ans = [0, 0]
go(0, 0, 0, 0)
go(1, 0, 0, 1)
print(sum(ans))
