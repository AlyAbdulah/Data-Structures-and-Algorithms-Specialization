def count_inversions(arr):
    if len(arr) == 1:
        return arr, 0

    mid = len(arr) // 2
    left_sorted, inv_left = count_inversions(arr[:mid])
    right_sorted, inv_right = count_inversions(arr[mid:])
    merged_arr, inv_merge = merge_inversions(left_sorted, right_sorted)

    total_inversions = inv_left + inv_right + inv_merge
    return merged_arr, total_inversions


def merge_inversions(sorted_arr1, sorted_arr2):
    merged_arr = []
    inversions, i, j = 0, 0, 0

    while i < len(sorted_arr1) and j < len(sorted_arr2):
        if sorted_arr1[i] <= sorted_arr2[j]:
            merged_arr.append(sorted_arr1[i])
            i += 1
        else:
            merged_arr.append(sorted_arr2[j])
            j += 1
            inversions += len(sorted_arr1[i:])

    merged_arr.extend(sorted_arr1[i:])
    merged_arr.extend(sorted_arr2[j:])
    return merged_arr, inversions


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(count_inversions(arr)[1])
