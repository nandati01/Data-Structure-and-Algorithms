from collections import defaultdict
def subarray_sum(nums, k):
    """
    Given an integer array nums and an integer k
    Return number of subarrays whose sum is equal to k
    """
    #declaring our hash map counts
    #counts maps prefix sums to their frequency
    counts = defaultdict(int)
    #Empty prefix sum has a sum of 0
    #so initializing {0:1}
    counts[0] = 1
    #curr is the sum of all elements we have iterated so far
    ans = curr = 0
    for num in nums:
        curr += num
        #curr is the sum up to any index i
        #if there is an index j whose prefix is curr - k
        #sum of subarray with elements from j + 1 to i is curr - (curr - k) = k
        ans += counts[curr - k]
        #updating counts for the current prefix sum
        counts[curr] += 1
    return ans
print(subarray_sum([1, 2, 1, 2, 1], 3))
