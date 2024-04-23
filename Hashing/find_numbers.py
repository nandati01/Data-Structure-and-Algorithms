def find_numbers(nums):
    """
    Given an integer array nums
    Return all the unique numbers in nums that satisfies the following:
    x + 1 and x - 1 both are not in nums
    """

    ans = []
    nums = set(nums)

    for num in nums:
        if (num + 1 not in nums) and (num - 1 not in nums):
            ans.append(num)
    return ans 