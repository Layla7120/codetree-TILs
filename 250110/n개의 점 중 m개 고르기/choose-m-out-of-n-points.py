import sys


def dist(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax - bx) ** 2 + abs(ay - by) ** 2

def get_max_dist(num_list):
    max_dist = 0
    for i in range(len(num_list)):
        for j in range(i, len(num_list)):
            distance = dist(dots[num_list[i]], dots[num_list[j]])
            if distance > max_dist:
                max_dist = distance

    return max_dist


def choose(curr_num, cnt):
    global candidate, global_min_of_max_distances
    if curr_num == n:
        if cnt == m:
            max_dist = get_max_dist(candidate)
            if global_min_of_max_distances > max_dist:
                global_min_of_max_distances = max_dist
        return

    candidate.append(curr_num)
    choose(curr_num + 1, cnt + 1)
    candidate.pop()

    choose(curr_num + 1, cnt)


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    dots = [list(map(int, input().split())) for _ in range(n)]

    global_min_of_max_distances = sys.maxsize

    candidate = []

    choose(0, 0)
    print(global_min_of_max_distances)