n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))

answer = []
max_num = 0


def calculate_xor(A):
    global max_num
    ans = A[0]
    for i in range(1, len(A)):
        ans = ans ^ A[i]
    if ans > max_num:
        max_num = ans


def choose(curr_num, cnt):
    if curr_num == n + 1:
        if cnt == m:
            final_nums = [nums[i - 1] for i in answer]
            calculate_xor(final_nums)
        return

    answer.append(curr_num)
    choose(curr_num + 1, cnt + 1)
    answer.pop()

    choose(curr_num + 1, cnt)

    return


choose(1, 0)

print(max_num)