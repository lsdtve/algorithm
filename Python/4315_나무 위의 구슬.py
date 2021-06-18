def dfs(index):
    if leaf[index]:
        return node[index]

    for i in child[index]:
        ans[index] += abs(dfs(i)-1)
        node[index] += node[i] - 1
    return node[index]


while True:
    N = int(input())
    if N == 0:
        break

    node = [0] * (N+1)
    parent = [0] * (N+1)
    ans = [0] * (N+1)
    child = [[] for _ in range(N+1)]
    leaf = [False] *(N+1)

    for i in range(1,N+1):
        s = list(map(int, input().split()))
        node[s[0]] = s[1]
        if s[2] == 0:
            leaf[s[0]] = True
        for j in range(s[2]):
            parent[s[3+j]] = s[0]
            child[s[0]].append(s[3+j])

    for i in range(1,N+1):
        if parent[i] == 0:
            dfs(i)
            break
    print(sum(ans))