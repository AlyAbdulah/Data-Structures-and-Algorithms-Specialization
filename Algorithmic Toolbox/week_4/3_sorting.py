from numpy import random
import sys

sys.setrecursionlimit(200000)


def majority_element_fast_count(arr):
    element_count = {}
    for element in arr:
        if element not in element_count:
            element_count[element] = 1
        else:
            element_count[element] += 1

    majority_threshold = len(arr) // 2 + 1
    for key, value in element_count.items():
        if value >= majority_threshold:
            return key, value
    return -1, -1


def majority_element_divide_and_conquer_count(arr, left, right):
    if left == right:
        return arr[left], 1
    else:
        mid = (left + right) // 2

        left_majority, count_left_majority = majority_element_divide_and_conquer_count(arr, left, mid)
        right_majority, count_right_majority = majority_element_divide_and_conquer_count(arr, mid + 1, right)

        if left_majority == right_majority:
            if left_majority == -1:
                return -1, -1
            else:
                return left_majority, count_left_majority + count_right_majority

        count_left_majority += sum(1 for i in range(mid + 1, right + 1) if arr[i] == left_majority)
        count_right_majority += sum(1 for i in range(left, mid + 1) if arr[i] == right_majority)

        majority_threshold = (right - left + 1) // 2 + 1
        if count_left_majority >= majority_threshold:
            return left_majority, count_left_majority
        elif count_right_majority >= majority_threshold:
            return right_majority, count_right_majority
        else:
            return -1, -1


def stress_test():
    i = 0
    while True:
        N = random.randint(1, 10)
        arr = random.randint(0, 5, size=N)

        print(i)

        fast_majority, fast_count = majority_element_fast_count(arr)
        div_and_conq_majority, div_and_conq_count = majority_element_divide_and_conquer_count(arr, 0, len(arr) - 1)

        if fast_majority != div_and_conq_majority:
            print("Array:", arr)
            print("Fast algorithm:", fast_majority)
            print("Divide & conquer algorithm:", div_and_conq_majority)
            break

        i += 1


if __name__ == "__main__":
    # stress_test()

    n = int(input())
    arr = list(map(int, input().split()))
    if majority_element_divide_and_conquer_count(arr, 0, n - 1)[0] != -1:
        print(1)
    else:
        print(0)
