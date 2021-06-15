import sys
read = sys.stdin.readline

N = int(input())
array = list(map(int, read().split()))
array.sort()
ans_sum = 99999999999999999
ans_list = []
for i in range(N):
    j = i + 1
    t = N - 1
    while True:
        if j >= t:
            break
        tot = array[i] + array[j] + array[t]
        if abs(tot) < ans_sum:
            ans_sum = abs(tot)
            ans_list = [array[i], array[j], array[t]]

        if tot > 0:
            t -= 1
        else:
            j += 1

print(*ans_list)
