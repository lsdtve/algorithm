def go(index):
    if check():
        return

    if array[index] < 5:
        array[index] = 5
        go(index+1)
    else:
        array[index + 1] += 1
        temp = 1
        while True:
            if array[index + temp] >= 10:
                array[index + temp + 1] += 1
                array[index + temp] = 0
                temp += 1
            else:
                break
        if check():
            array[index] = 0
            return
        array[index] = 5
        go(index+1)


def check():
    cnt = 0
    for i in array:
        if i == 5:
            cnt += 1

    if cnt >= K:
        return True
    return False


N, K = map(int, input().split())
array = list(reversed(list(map(int, str(N+1))))) + [0]*15
go(0)
for i in range(len(array)-1,-1,-1):
    if array[i] != 0:
        print(*reversed(array[:i+1]), sep="")
        break