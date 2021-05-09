def find(a):
    if p[a] == a:
        return a
    p[a] = find(p[a])
    return p[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

V, E = map(int, input().split())
p = [i for i in range(V + 1)]
graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key=lambda x: x[2])

ans = 0
edge_count = 0
for e in graph:
    if edge_count == V-1:
        break
    a, b, c = e
    if find(a) != find(b):
        union(a, b)
        ans += c
        edge_count += 1
print(ans)