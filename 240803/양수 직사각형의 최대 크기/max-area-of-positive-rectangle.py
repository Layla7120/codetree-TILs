import sys

n, m = map(int, sys.stdin.readline().split())
board = []

for y in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

def find_square(n, m):
    max_size = 0
    for x in range(m):
        for y in range(n):
            if board[x][y] > 0:
                width = 1
                for i in range(y + 1, n):
                    if board[x][i] > 0:
                        width += 1
                    else:
                        break
                height = 1
                for j in range(x + 1, m):
                    count = 0
                    for x in range(y, y + width):
                        if board[j][x] > 0:
                            count += 1
                        else:
                            break
                    if count == 0:
                        if max_size < width * height:
                            max_size = width * height
                        break
                    else:
                        width = count
                        height += 1
            if max_size < width * height:
                            max_size = width * height  
    return max_size

print(find_square(n, m))