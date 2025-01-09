N, M = map(int, input().split())

# Write your code here!
n = 3
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(curr_num, cnt):
    if curr_num == n + 1:
        if cnt == m:
            print_answer()
        return

    answer.append(0)
    choose(curr_num + 1, cnt)
    answer.pop()

    answer.append(1)
    choose(curr_num + 1, cnt + 1  )
    answer.pop()

    return

choose(1)