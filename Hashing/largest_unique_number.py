def largest_unique_number(nums):
    """
    Given an integer array nums
    Return the largest integer that only occurs once
    Else return -1
    """
    lst = [num for num in nums if nums.count(num) == 1]
    return max(lst) if lst else -1
nums = [5,7,3,9,4,9,8,3,1]
print(largest_unique_number(nums))
nums = [9,9,8,8]
print(largest_unique_number(nums))
