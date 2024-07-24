import sys

n = int(sys.stdin.readline())
points = []

for i in range(n):
    points.append(list(map(int, sys.stdin.readline().split())))

min_len = sys.maxsize
for i in range(1, n - 1):
    sum_len = 0
    new_points = points[:i] + points[i+1:]
    for j in range(1, n - 1):
        sum_len += abs(new_points[j][0] - new_points[j-1][0]) + abs(new_points[j][1] - new_points[j-1][1])
    if sum_len < min_len:
        min_len = sum_len

print(min_len)