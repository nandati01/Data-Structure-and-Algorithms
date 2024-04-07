def split_array(nums):
    """Given an integer array nums
    Find number of ways to split the array in two
    First section should have sum greater than or equal to the second one
    Second section should have at least one number
    """
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    result = 0
    #because there needs to be at least one element on the second segment
    for i in range(len(nums)-1):
        left_section = prefix[i]
        #right section is prefix sum of last element - prefix sum of the left section
        right_section = prefix[-1] - prefix[i]
        if left_section >= right_section:
            result += 1
    return result 

#An alternate way to find the ways to split the array in two
def split_array_alt(nums):
    result = 0
    #initialize left section to 0 and calculate it on the fly
    left_section = 0
    #find right section by subtracting the total sum by left section
    total = sum(nums)

    #right section needs at least one element
    #stopping before the last element
    for i in range(len(nums) - 1):
        left_section += nums[i]
        right_section = total - left_section
        if left_section >= right_section:
            result += 1
    return result

test_cases = [
    [1, 2, 3, 4],
    [10, 4, 1, 2],
    [1, 1, 1, 1, 1],
    [10],
    [5, 2, 3],
    [10, 4, -8, 7]
]

result = [(split_array(test_case), split_array_alt(test_case)) for test_case in test_cases]
print(result)
