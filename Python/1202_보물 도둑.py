import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewelry = []

for _ in range(N):
    heapq.heappush(jewelry, list(map(int, sys.stdin.readline().split())))

bags = [int(sys.stdin.readline()) for _ in range(K)]

bags.sort()

ans = 0
temp = []
for bag in bags:
    while jewelry and bag >= jewelry[0][0]:
        heapq.heappush(temp, -heapq.heappop(jewelry)[1])
    if temp:
        ans += -heapq.heappop(temp)
    elif not jewelry:
        break

print(ans)