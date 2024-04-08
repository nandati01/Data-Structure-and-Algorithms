def get_averages(nums, k):
    """
    Given an array nums of length n and an integer k 
    Return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i
    The k-radius average at position i involves finding
    mean of numbers between i - k and i + k (inclusive)
    If there are less than k elements before or after the index i
    then k-radius average is -1
    """
    #if the radius is 0, return the array
    if k == 0:
        return nums
    #finding the prefix sum
    prefix = []
    n = len(nums)
    sums = 0
    for num in nums:
        sums += num
        prefix.append(sums)
    #initializing the average with all -1s
    avgs = [-1]*n
    denom = 2 * k + 1 #total number of elements in the subarray
    #if window size is larger than the array, return -1
    if denom > n:
        return avgs
    for i in range(n):
        start = i - k
        end = i + k
        if start >= 0 and end < n:
            avgs[i] = (prefix[end] - prefix[start] + nums[start])//denom
    return avgs

test_cases = [
    ([1, 3, 5, 7, 9], 1),
    ([1, 3, 5, 7, 9, 11], 2),
    ([], 1),
    ([10], 0),
    ([1, 2, 3, 4, 5], 0),
    ([7,4,3,9,1,8,5,2,6], 3)
]

test_outcome = []

for nums, k in test_cases:
    result = get_averages(nums, k)
    test_outcome.append(result)
print(test_outcome)
