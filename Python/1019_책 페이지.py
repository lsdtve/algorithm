def cal(n, point):
    while 0 < n:
        count[int(n % 10)] += point
        n //= 10

N = int(input())
start = 1
count = [0] * 10
point = 1

while start <= N:
    while N % 10 != 9 and start <= N:
        cal(N, point)
        N -= 1
    while start % 10 != 0 and start <= N:
        cal(start, point)
        start += 1

    if N < start:
        break

    start //= 10
    N //= 10

    for i in range(10):
        count[i] += (N - start + 1) * point
    point *= 10
print(*count)