import sys

n, k = map(int, sys.stdin.readline().split())
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(curr_num):
    if curr_num == k + 1:
        print_answer()
        return
    
    for i in range(1, n + 1):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

choose(1)