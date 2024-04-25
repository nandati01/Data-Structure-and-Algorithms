from collections import defaultdict

def intersection(nums):
    """
    Given a 2D array nums that contains n arrays of distinct integers
    Return a sorted array containing all the numbers that appear in all n arrays
    For example: nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
    Return [3, 4]
    """
    counts = defaultdict(int) #dict with a default value of 0
    for arr in nums: #for each arr inside the array nums
        for x in arr: #for each element in arr
            counts[x] += 1 #count of each element is updated
    n = len(nums) #number of arrays in nums
    ans = []
    for key in counts:
        #since it is an array of distinct integers
        if counts[key] == n: #if element appears in all the arrays
            ans.append(key)
    return sorted(ans)

nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
print(intersection(nums))
