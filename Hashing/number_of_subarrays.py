from collections import defaultdict
def num_of_subarrays(nums, k):
    """
    Given an array of positive integers nums and integer k
    Return the number of subarrays with exactly k odd numbers in them
    """
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0
    for num in nums:
        curr += num % 2
        ans += counts[curr - k]
        counts[curr] += 1
    return ans

print(num_of_subarrays([1, 1, 2, 1, 1], 3))
