def missing_number(nums):
    """
    Given an array nums containing n distinct numbers in the range [0, n]
    Return the only number in the range that is missing from the array
    """
    nums.sort()
    for i, num in enumerate(nums):
        if num != i:
            return i
    return len(nums)
nums = [9,6,4,2,3,5,7,0,1]
print(missing_number(nums))
nums = [0,1]
print(missing_number(nums))
