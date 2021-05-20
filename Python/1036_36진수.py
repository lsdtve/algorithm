import string

tmp = string.digits + string.ascii_uppercase
def convert(num, base):
    a = num // base
    r = num % base
    if a == 0:
        return tmp[r]
    else:
        return convert(a, base) + tmp[r]

n = int(input())
array = [input().strip() for _ in range(n)]
k = int(input())
tot = 0
diff = [0] * 36
for value in array:
    tot += int(value, 36)
    size = len(value)
    for (t, c) in enumerate(value):
        index = size - t - 1
        diff[int(c, 36)] += int(pow(36, index) * (35 - int(c, 36)))
diff.sort(reverse=True)
print(convert(tot + sum(diff[:k]), 36))