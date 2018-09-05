# Given a non-empty array of integers, return the third maximum number in this array.
# If it does not exist, return the maximum number. The time complexity must be in O(n).


def thirdMax(nums):
    if len(set(nums)) < 3:
        return max(nums)

    max_num = nums[0]
    max_2 = -2**32
    max_3 = -2**32

    for num in set(nums[1:]):
        if num > max_num:
            max_3 = max_2
            max_2 = max_num
            max_num = num
        elif num < max_num and num > max_3:
            if num > max_2:
                max_3 = max_2
                max_2 = num
            elif num < max_2:
                max_3 = num
        elif num < max_num and num < max_3:
            if num > max_3:
                max_2 = max_3
                max_3 = num
    return max_3
