import sys

def cal_diff(first_group):
    global min_diff

    group_a = 0
    group_b = 0

    for i in range(len(num)):
        if i in first_group:
            group_a += num[i]
        else:
            group_b += num[i]

    if abs(group_a - group_b) < min_diff:
        min_diff = abs(group_a - group_b)


def choose(curr_num, cnt):
    if curr_num == len(num):
        if cnt == n:
            cal_diff(first_group)
        return

    first_group.append(curr_num)
    choose(curr_num + 1, cnt + 1)
    first_group.pop()

    choose(curr_num + 1, cnt)

    return

if __name__ == '__main__':
    n = int(input())
    num = list(map(int, input().split()))

    first_group = []
    min_diff = sys.maxsize

    choose(0, 0)
    print(min_diff)
