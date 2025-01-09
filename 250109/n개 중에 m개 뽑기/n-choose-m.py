N, M = map(int, input().split())

# Write your code here!
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(curr_num):
    if curr_num == M + 1:
        print_answer()
        return

    for i in range(1,  N + 1):
        if len(answer) == 0 or answer[-1] < i:
            answer.append(i)
            choose(curr_num + 1)
            answer.pop()

    return

choose(1)