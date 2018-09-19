def find_max_consecutive_ones(nums):
    max_ones = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count = current_count + 1

            if current_count > max_ones:
                max_ones = current_count

        elif num == 0:

            if current_count > max_ones:
                max_ones = current_count

            current_count = 0

    return max_ones
