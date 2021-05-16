import sys
read = sys.stdin.readline

def binary_search(start, end, target):
    if start > end:
        return
    mid = (start + end) // 2
    diff = array[target] + array[mid]

    global ansDiff, ansNum
    if abs(diff) < ansDiff:
        ansDiff = abs(diff)
        ansNum = [array[mid], array[target]]

    if diff > 0:
        binary_search(start, mid-1, target)
    else:
        binary_search(mid+1, end, target)


N = int(read())
array = list(map(int, read().split()))
ansDiff = abs(array[0] + array[1])
ansNum = array[:2]

for i in range(N):
    binary_search(i+1, N-1, i)

ansNum.sort()
print(ansNum[0], ansNum[1])
