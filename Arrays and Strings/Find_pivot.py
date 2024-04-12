def find_pivot_index(nums):
    """
    Given an array of integers
    Return pivot index such that the sum of all elements strictly to the left
    is equal to the sum of all elements strictly to the right of the pivot
    If no such index exists, return -1
    """
    total = sum(nums)
    left = 0
    for i, num in enumerate(nums):
        right = total - left - num
        if right == left:
            return i
        left += num
    return -1

test_cases = [
    [1, 7, 3, 6, 5, 6],  # Expected output: 3
    [1, 2, 3],            # Expected output: -1
    [2, 1, -1],           # Expected output: 0
    [-1, -1, -1, 0, 1, 1], # Expected output: 0
    [],                   # Empty array: -1
    [100],                     # Single element array
    [0, 0, 0, 0, 0, 0],        # Arrays with all zeros
    [1, 1, 1, 1, 2, 2, 2],     # Arrays where pivot is exactly in the middle
    [-10, 20, -10],            # Negative and positive numbers balance
    [1000000, 1000000, -1000000], # Large numbers
    [1, 1, 1, 1, 1]            # All elements are the same (except boundaries)
]

# Applying the function to the test cases
results = [find_pivot_index(case) for case in test_cases]
print(results)
