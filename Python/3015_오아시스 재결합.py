import sys
read = sys.stdin.readline

N = int(read())
stack = []
ans = 0
for i in range(N):
    n = int(read())

    cnt = 1
    while stack:
        if stack[-1][0] == n:
            ans += stack[-1][1]
            cnt = stack[-1][1] + 1
            stack.pop()
        elif stack[-1][0] < n:
            ans += stack[-1][1]
            cnt = 1
            stack.pop()
        else:
            ans += 1
            break
    stack.append([n, cnt])

print(ans)