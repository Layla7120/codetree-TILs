import sys

n = int(sys.stdin.readline())
total = 0
num_arr = []


# 아름다운 지 확인
def is_beautiful(num_arr):
    global total
    pin_start = 0
    idx = 0
    while True:
        if pin_start + idx >= len(num_arr):
            break
        if num_arr[pin_start] == num_arr[pin_start + idx]:
            idx += 1
        else:
            if idx % num_arr[pin_start]:
                return False
            else:
                pin_start = pin_start + idx
                idx = 0
    if idx % num_arr[pin_start]:
        return False
    return True


# 재귀 부분

def recursion(count):
    global total
    if count == n:
        if is_beautiful(num_arr):
            total += 1
        return

    for i in range(1, 5):
        num_arr.append(i)
        recursion(count + 1)
        num_arr.pop()


recursion(0)
print(total)