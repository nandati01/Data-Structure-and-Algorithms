def find_max_average(nums, k):
    """Given an integer nums with length n and an integer k
    Find a subarray whose length is equal to k that has the maximum average value
    Return the maximum average value
    """
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k

# Test case 1: Simple case
nums1 = [1, 12, -5, -6, 50, 3]
k1 = 4
print(find_max_average(nums1, k1))  # Expected: 12.75

# Test case 2: All negative numbers
nums2 = [-1, -12, -5, -6, -50, -3]
k2 = 2
print(find_max_average(nums2, k2))  # Expected: -5.5

# Test case 3: All positive numbers
nums3 = [5, 18, 7, 20, 19, 18]
k3 = 3
print(find_max_average(nums3, k3))  # Expected: 18.333333333333332

# Test case 4: Single element per window (k = 1)
nums4 = [4, 0, 10, -5]
k4 = 1
print(find_max_average(nums4, k4))  # Expected: 10.0

# Test case 5: The entire array (k equals the length of the array)
nums5 = [4, 0, 10, -5]
k5 = len(nums5)
print(find_max_average(nums5, k5))  # Expected: 2.25
