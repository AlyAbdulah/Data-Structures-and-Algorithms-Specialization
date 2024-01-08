from numpy import random

def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def stress_test():
    flag_correct = True
    i = 0
    while flag_correct:
        N = random.randint(1, 10)
        x = random.randint(1, 10)
        arr = random.randint(0, 10, size=N)
        arr.sort()

        print(i, arr, x, N)

        ls_res = linear_search(arr, x)
        bs_res = binary_search(arr, x)

        if ls_res != bs_res:
            print(i, arr, x, N)
            print('Linear search:', ls_res)
            print('Binary search:', bs_res)
            flag_correct = False

        i += 1

if __name__ == '__main__':
    # Uncomment the following line to perform stress testing
    # stress_test()

    # Input format: first line contains the number of elements, followed by the array elements
    arr = list(map(int, input().split()))[1:]
    
    # Next line contains the number of values to search for, followed by the values
    val = list(map(int, input().split()))[1:]

    for v in val:
        print(binary_search(arr, v), end=' ')
