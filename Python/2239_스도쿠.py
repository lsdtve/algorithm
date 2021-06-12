def go(cnt):
    if cnt == 81:
        return True
    y = cnt // 9
    x = cnt % 9

    if array[y][x] == 0:
        num_list = find_num_list(x, y)
        if not num_list:
            return False

        for i in num_list:
            array[y][x] = i
            if go(cnt + 1):
                return True
            array[y][x] = 0
    else:
        if go(cnt + 1):
            return True


def find_num_list(x,y):
    check = [False]*10
    for i in range(9):
        check[array[i][x]] = True
        check[array[y][i]] = True
    for i in range((y//3)*3, (y//3 + 1)*3):
        for j in range((x//3)*3, (x//3 + 1)*3):
            check[array[i][j]] = True
    return [i for i in range(1,10) if not check[i]]


array = [list(map(int, input())) for _ in range(9)]
go(0)
for i in array:
    print(*i,sep="")