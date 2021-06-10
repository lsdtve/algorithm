import sys
read = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = array[start]
        return array[start]
    mid = (start + end) // 2

    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]


def subSum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return subSum(start, mid, node*2, left, right) + subSum(mid+1, end, node*2+1, left, right)


def update(start, end, node, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node*2, index, diff)
    update(mid+1, end, node*2+1, index, diff)


N, M, K = map(int, read().split())
array = [0] * N
tree = [0] * (N*4)

for i in range(N):
    array[i] = int(read())
init(0, N-1, 1)

for i in range(M+K):
    a, b, c = map(int, read().split())
    if a == 1:
        diff = c - array[b-1]
        array[b-1] = c
        update(0, N-1, 1, b-1, diff)
    else:
        print(subSum(0,N-1,1,b-1,c-1))