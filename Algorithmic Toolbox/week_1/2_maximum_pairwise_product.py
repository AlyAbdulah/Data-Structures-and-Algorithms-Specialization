def max_pair_product(nums):
    if (len(nums) >= 2):
        nums.sort(reverse=True)
        return nums[0] * nums[1]
    else:
        return None

if __name__ == '__main__':
    item = int(input())
    nums = map(int, input().split())
    print(max_pair_product(list(nums)))