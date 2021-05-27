MIN, MAX = map(int, input().split())
tot = MAX - MIN + 1
ans = [True] * tot

cnt = 2
while True:
    temp = cnt**2
    if temp > MAX:
        break
    n = temp * (MIN // temp)
    if MIN > n:
        n += temp
    n -= MIN
    for i in range(n, tot, temp):
        ans[i] = False
    cnt += 1
print(sum(ans))
