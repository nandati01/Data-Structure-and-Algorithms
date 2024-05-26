def contains_duplicate(nums):
    """
    Given an integer array nums
    Return True if any value appears at least twice in the array
    False if every array is distinct
    """
    return len(set(nums)) != len(nums)

test_cases = [
    # Test cases where the expected result is False
    {"input": [], "expected": False},              # Empty array
    {"input": [1], "expected": False},             # Single element array
    {"input": [1, 2, 3, 4, 5], "expected": False}, # No duplicates
    {"input": list(range(10000)), "expected": False}, # Large array with no duplicates

    # Test cases where the expected result is True
    {"input": [1, 2, 3, 2], "expected": True},     # Array with duplicates
    {"input": [1, 1, 1, 1], "expected": True},     # All elements are duplicates
    {"input": list(range(9999)) + [0], "expected": True}, # Large array with duplicates
]
for case in test_cases:
    result = contains_duplicate(case["input"])
    assert result == case["expected"], f"Test failed for input {case['input']}. Expected {case['expected']}, got {result}"
print("All tests passed!")
