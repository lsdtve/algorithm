import sys
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree_max[node] = array[start]
        tree_min[node] = array[start]
        return
    mid = (start + end) // 2

    init(start, mid, node*2)
    init(mid+1, end, node*2 + 1)
    tree_max[node] = max(tree_max[node*2], tree_max[node*2 + 1])
    tree_min[node] = min(tree_min[node*2], tree_min[node*2 + 1])


def find(start, end, node, left, right):
    if right < start or end < left:
        return [0, 1_000_000_001]
    if left <= start and end <= right:
        return [tree_max[node], tree_min[node]]
    mid = (start + end) // 2
    l = find(start,mid,node*2,left,right)
    r = find(mid+1,end,node*2+1,left,right)
    return [max(l[0],r[0]), min(l[1],r[1])]


N, M = map(int, input().split())
array = [int(input()) for _ in range(N)]
tree_max = [0] * (N*4)
tree_min = [1_000_000_001] * (N*4)
init(0, N-1, 1)
for i in range(M):
    a, b = map(int, input().split())
    result = find(0,N-1,1,a-1,b-1)
    print(result[1], result[0])