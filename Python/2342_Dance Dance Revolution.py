import sys
sys.setrecursionlimit(10**6)


def go(left, right, index):
    if index == N:
        return 0

    if dp[index][left][right]:
        return dp[index][left][right]

    dp[index][left][right] = min(
        move(left, array[index]) + go(array[index], right, index + 1),
        move(right, array[index]) + go(left, array[index], index + 1)
    )

    return dp[index][left][right]


def move(now, next):
    if now == next:
        return 1
    if now == 0:
        return 2
    if now == 1:
        return 4 if next == 3 else 3
    if now == 2:
        return 4 if next == 4 else 3
    if now == 3:
        return 4 if next == 1 else 3
    if now == 4:
        return 4 if next == 2 else 3


array = list(map(int, input().split()))
N = len(array)-1
dp = [[[0]*5 for _ in range(5)] for _ in range(N+1)]
print(go(0,0,0))