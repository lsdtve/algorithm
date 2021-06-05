from collections import Counter

def go(x, y):
    left = []
    result = 0
    for ny in range(y-1, -1, -1):
        temp = 0
        for nx in range(x-1, -1, -1):
            temp += array[ny][nx]
            if ny != y-1:
                cache[ny][nx] = cache[ny+1][nx] + temp
            else:
                cache[ny][nx] = temp
            left.append(cache[ny][nx])
    left = Counter(left)

    for ny in range(y, N):
        temp = 0
        for nx in range(x, N):
            temp += array[ny][nx]
            if ny != y:
                cache[ny][nx] = cache[ny-1][nx] + temp
            else:
                cache[ny][nx] = temp
            result += left.get(cache[ny][nx], 0)

    left = []
    for ny in range(y, N):
        temp = 0
        for nx in range(x-1, -1, -1):
            temp += array[ny][nx]
            if ny != y:
                cache[ny][nx] = cache[ny-1][nx] + temp
            else:
                cache[ny][nx] = temp
            left.append(cache[ny][nx])
    left = Counter(left)

    for ny in range(y-1, -1, -1):
        temp = 0
        for nx in range(x, N):
            temp += array[ny][nx]
            if ny != y-1:
                cache[ny][nx] = cache[ny+1][nx] + temp
            else:
                cache[ny][nx] = temp
            result += left.get(cache[ny][nx], 0)
    return result

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
cache = [[0]*N for _ in range(N)]
ans = 0
for y in range(1,N):
    for x in range(1,N):
        ans += go(x,y)
print(ans)
