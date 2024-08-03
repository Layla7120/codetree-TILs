import sys

n, m = map(int, sys.stdin.readline().split())
board = []

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

max_size = 0
for x in range(n):
    for y in range(m):
        if board[x][y] > 0:
            width = 0
            for i in range(y + 1, m):
                if board[x][i] > 0:
                    width += 1
                else:
                    break
            height = 0
            for j in range(x + 1, n):
                count = 0
                for k in range(y, y + width):
                    if board[j][k] > 0:
                        count += 1
                    else:
                        break
                if count == 0:
                    if max_size < width * height:
                        max_size = width * height
                    break
                else:
                    if count < width:
                        width = count
                    height += 1
            final_width = width + 1
            final_height = height + 1
            if max_size < final_width * final_height:
                max_size = final_width * final_height

print(max_size)