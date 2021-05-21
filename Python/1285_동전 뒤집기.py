import sys

N = int(sys.stdin.readline())
array = [list(sys.stdin.readline()) for _ in range(N)]
ans = 99999999
change = {"H": "T", "T": "H"}

for i in range(1 << N):
    temp = 0
    for x in range(N):
        tnum = 0
        for y in range(N):
            char = array[y][x]
            if (i & 1<<y) != 0:
                char = "H" if array[y][x] == "T" else "T"
            if char == "T":
                tnum += 1
        temp += min(N-tnum, tnum)
    ans = min(ans, temp)
print(ans)
