import sys
read = sys.stdin.readline

N, S = map(int, read().split())
lst = list(map(int, read().split()))

ans = sys.maxsize
tot = 0
start = 0
end = 0
while start != N:
    if tot >= S:
        ans = min(ans, end-start)
        tot -= lst[start]
        start += 1
    elif end >= N:
        break
    else:
        tot += lst[end]
        end += 1
print(0 if ans == sys.maxsize else ans)