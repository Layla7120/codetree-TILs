import copy
import sys

n = int(sys.stdin.readline())
mapper = {
    1: [[-1, 0], [-2, 0], [1, 0], [2, 0]],
    2: [[-1, 0], [1, 0], [0, 1], [0, -1]],
    3: [[-1, 1], [-1, -1], [1, 1], [1, -1]]
}

board = []
bomb_loc = []
bomb_combin = []
max_count = 0

# board 저장하고 폭탄 위치 저장
for i in range(n):
    new_rows = list(map(int, sys.stdin.readline().split()))
    for idx, n in enumerate(new_rows):
        if n:
            bomb_loc.append([i, idx])
    board.append(new_rows)


# 영역 내 인지 확인
def in_range(n, row: int, col: int):
    return 0 <= row < n and 0 <= col < n


# 폭파 지점 count +1 하고 board 에 -1 로 표시 하기
def bang(bomb_place: list[int], bomb_type: int, board_copy, count):
    bomb_row, bomb_col = bomb_place
    place = mapper[bomb_type]
    for n_row, n_col in place:
        new_row = n_row + bomb_row
        new_col = n_col + bomb_col
        if in_range(len(board_copy), new_row, new_col):
            if board_copy[new_row][new_col] == 0:
                board_copy[new_row][new_col] = -1
                count += 1
    return count, board_copy


def bang_All(bomb_com):
    global max_count
    total_count = 0
    board_copy = copy.deepcopy(board)
    for idx,bomb in enumerate(bomb_loc):
        total_count, board_copy = bang(bomb, bomb_com[idx], board_copy, total_count)
    if total_count > max_count:
        max_count = total_count

# 각 폭탄 실험해 보고 가장 많이 폭파한 영역 출력 하기
# 어느 폭탄 실험할 지 고를 때 재귀 사용


def pick_bomb(cnt):
    global bomb_combin, max_count

    if cnt == len(bomb_loc):
        bang_All(bomb_combin)
        return
    for bomb in range(1, 4):
        bomb_combin.append(bomb)
        pick_bomb(cnt + 1)
        bomb_combin.pop()


pick_bomb(0)
print(max_count + len(bomb_loc))