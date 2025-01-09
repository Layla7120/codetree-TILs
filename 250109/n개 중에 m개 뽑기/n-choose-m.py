N, M = map(int, input().split())

# Write your code here!
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(curr_num, cnt):
    if curr_num == N + 1:
        if cnt == M:
            print_answer()
        return

    answer.append(curr_num)
    choose(curr_num + 1, cnt + 1)
    answer.pop()

    # 패스하는 경우
    choose(curr_num + 1, cnt)

    return

choose(1, 0)