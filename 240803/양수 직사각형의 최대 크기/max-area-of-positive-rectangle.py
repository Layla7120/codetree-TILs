import sys

n, m = map(int, sys.stdin.readline().split())
board = []

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

max_size = 0
for row in range(n):
    for col in range(m):
        if board[row][col] > 0:
            # 가로 최대폭 구하기
            width = 1
            for i in range(col + 1, m):
                if board[row][i] > 0:
                    width += 1
                else:
                    break
            # 각각의 가로폭에서 최대 세로폭 구하기 최대 넓이 구하기
            for w in range(width + 1):
                height = 1
                for j in range(row + 1, n):
                    count = 0
                    for k in range(col, col + w):
                        if board[j][k] > 0:
                            count += 1
                        else:
                            break
                    if count == 0 or count != w:
                        break
                    else:
                        height += 1
                if max_size < w * height:
                    max_size = w * height

if max_size == 0:
    max_size = -1

print(max_size)