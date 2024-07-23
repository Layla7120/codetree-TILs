import sys

n = int(sys.stdin.readline())

board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
 
max_count = 0

for i in range(n):
    for j in range(n - 2):
        count = 0
        for k in range(3):
            if board[i][j + k] == 1:
                count += 1
        if count > max_count:
            max_count = count

print(max_count)