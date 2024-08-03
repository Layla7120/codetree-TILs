import sys

n, m = map(int, sys.stdin.readline().split())
board = []

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

max_size = 0
for row in range(n):
    for col in range(m):
        if board[row][col] > 0:
            width = 0
            for i in range(col + 1, m):
                if board[row][i] > 0:
                    width += 1
                else:
                    break
            height = 1
            for j in range(row + 1, n):
                count = 0
                for k in range(col, col + width + 1):
                    if board[j][k] > 0:
                        count += 1
                    else:
                        break
                if count == 0:
                    break
                else:
                    if count < width:
                        width = count
                    height += 1
            final_width = width + 1
            final_height = height

            if max_size < final_width * final_height:
                max_size = final_width * final_height
if max_size == 0:
    max_size = -1

print(max_size)