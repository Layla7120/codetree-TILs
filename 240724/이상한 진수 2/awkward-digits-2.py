import sys

n = sys.stdin.readline()

max_num = 0

for idx, i in enumerate(n):
    new_n = int(n, 2)
    if i == '0':
        new_n += 2 ** (len(n) - 1 - idx)
        if new_n > max_num:
            max_num = new_n
    else:
        new_n -= 2 ** (len(n) - 1 - idx)
        if new_n > max_num:
            max_num = new_n
print(max_num)