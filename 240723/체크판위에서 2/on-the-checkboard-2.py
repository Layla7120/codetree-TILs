import sys

R, C = map(int, sys.stdin.readline().split())

board = []
for _ in range(R):
    board.append(sys.stdin.readline().split())

count = 0
for i in range(1, R - 2):
    for j in range(1, C - 2):
        for k in range(i + 1, R - 1):
            for n in range(j + 1, C - 1):
                if board[0][0] != board[i][j] and board[i][j] != board[k][n] and board[k][n] != board[R - 1][C - 1]:
                    count += 1

print(count)