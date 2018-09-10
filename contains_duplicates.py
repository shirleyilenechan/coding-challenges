# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.


def contains_duplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        else:
            num_set.add(num)
    return False
