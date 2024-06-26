from collections import defaultdict
def max_subarray_length(nums, k):
    """
    Given an integer array nums and an integer k
    An array is good if the frequency of each element in this array is less than or equal to k
    Return the length of the longest good subarray of nums
    """
    left = max_length = over_k_counter = 0
    frequency = defaultdict(int)
    for right in range(len(nums)):
        frequency[nums[right]] += 1
        if frequency[nums[right]] > k:
            over_k_counter += 1
        while over_k_counter > 0:
            if frequency[nums[left]] > k:
                over_k_counter -= 1
            frequency[nums[left]] -= 1
            if frequency[nums[left]] == 0:
                del frequency[nums[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

print(max_subarray_length([1, 2, 3, 1, 2, 3, 1, 2], 2))  # Output: 6
print(max_subarray_length([1, 2, 1, 2, 1, 2, 1, 2], 1))  # Output: 2
print(max_subarray_length([5, 5, 5, 5, 5, 5, 5], 4))      # Output: 4
