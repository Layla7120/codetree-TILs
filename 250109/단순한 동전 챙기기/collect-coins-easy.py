import sys


def distance(before, after):
    b_x, b_y = before
    a_x, a_y = after
    return abs(b_x - a_x) + abs(b_y - a_y)

def get_total_distance(visit_queue):
    total = distance(start, visit_queue[0])
    for v in range(1, len(visit_queue)):
        total += distance(visit_queue[v], visit_queue[v - 1])
    total += distance(visit_queue[-1], end)
    return total

def choose(curr_idx, cnt):
    global min_dist

    if curr_idx == len(num_list):
        if cnt >= 3:
            dist = get_total_distance(visit_queue)
            if dist < min_dist:
                min_dist = dist
        return

    visit_queue.append(num_dict[num_list[curr_idx]])
    choose(curr_idx + 1, cnt + 1)
    visit_queue.pop()

    choose(curr_idx + 1, cnt)
    return


if __name__ == '__main__':
    n = int(input())
    grid = [list(input()) for _ in range(n)]

    visit_queue = []

    num_dict = {}
    num_list = []
    start = ()
    end = ()

    min_dist = sys.maxsize

    for i in range(n):
        for j in range(n):
            if grid[i][j].isdigit():
                num_dict[grid[i][j]] = (i, j)
                num_list.append(grid[i][j])
            if grid[i][j] == 'S':
                start = (i, j)
            if grid[i][j] == 'E':
                end = (i, j)

    if len(num_list) < 3:
        print(-1)
    else:
        num_list.sort()
        choose(0, 0)
        print(min_dist)