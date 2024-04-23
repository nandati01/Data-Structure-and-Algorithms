def two_sum(nums, target):
    """
    Given an array nums and a target
    Return indices of two numbers such that they add up to the target
    The total time complexity needs to be O(1)
    """
    dic = {}
    for i, num in enumerate(nums):
        #checking for target - num is O(1)
        complement = target - num
        if complement in dic:
            return [i, dic[complement]]
        dic[num] = i
    return [-1, -1]
nums = [5, 2, 7, 10, 3, 9]
print(two_sum(nums, 8))
