def longest_subarray(nums, k):
    """
    Given an array of positive integers nums and a target k
    Find the length of the longest subarray whose sum <= k
    """

    left = 0
    window_sum = 0
    length = 0

    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum > k:
            window_sum -= nums[left]
            left += 1
        length = max(length, right - left + 1)
    return length

def test_longest_subarray():
    """
    test cases to check the longest_subarray function
    """
    test_cases = [
        ([1, 2, 3, 4, 5], 10, 4),  # All elements sum up to less than or equal to 10
        ([3, 4, 1, 7, 2], 10, 3),  # Longest subarray: [4, 1, 7]
        ([10, 20, 30], 15, 1),     # All elements are greater than the target sum
        ([], 5, 0),                # Empty array
        ([2, 2, 2, 2], 5, 2),      # All elements sum up to less than or equal to 5
        ([5, 5, 5, 5], 5, 1),      # Single element less than or equal to the target sum
        ([1, 2, 3, 4, 5], 2, 1),   # Only one element less than or equal to the target sum
    ]

    for nums, k, expected in test_cases:
        result = longest_subarray(nums, k)
        assert result == expected, f"Test case failed: Input: {nums}, Target: {k}. Expected: {expected}, Got: {result}"

    print("All test cases passed!")

test_longest_subarray()
