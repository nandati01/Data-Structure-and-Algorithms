def min_subarray(nums, target):
    """
    Given an array of positive integers and a target
    Return the minimal length of subarray whose sum is greater than or equal to target
    """
    left = current_sum = 0
    min_length = len(nums) + 1
    for right, num in enumerate(nums):
        current_sum += num
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    return min_length if min_length <= len(nums) else 0

test_cases = [
        ([2, 3, 1, 2, 4, 3], 7, 2),  # Subarray [4, 3] or [3, 1, 2, 4] meets the target
        ([1, 4, 4], 4, 1),          # Exact match with single element
        ([1, 1, 1, 1, 1, 1, 1, 1], 8, 8),  # Entire array needed to meet the target
        ([5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 15, 2),  # Best subarray [10, 7]
        ([1, 2, 3, 4, 5], 15, 5),   # Entire array just meets the target
        ([1, 2, 3, 4, 5], 16, 0),   # No subarray can meet the target
        ([], 1, 0),                 # Empty array
        ([1, 2, 3, 4, 5], 1, 1)     # Minimum element meets the requirement
    ]

for nums, target, expected in test_cases:
    result = min_subarray(nums, target)
    assert result == expected, f"Failed on test with nums={nums} and target={target}. Expected {expected}, got {result}"

print("All cases passed!")
