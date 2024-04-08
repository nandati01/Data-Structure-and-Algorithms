def prefix_sum(num):
    """
    Given array nums
    Find prefix sum 
    """

    prefix = [num[0]]

    for i in range(1, len(num)):
        prefix.append(num[i] + prefix[-1])
    return prefix

def running_sum(num):
    """An alternate to prefix sum"""
    curr = 0
    sums = []
    for i in num:
        curr += i
        sums.append(curr)
    return sums

test_cases = [
    {
        "nums": [1, 2, 3, 4, 5],
        "expected_prefix": [1, 3, 6, 10, 15]
    },
    {
        "nums": [-1, 2, -3, 4, -5],
        "expected_prefix": [-1, 1, -2, 2, -3]
    },
    {
        "nums": [0, 0, 0, 0, 0],
        "expected_prefix": [0, 0, 0, 0, 0]
    },
    {
        "nums": [1000000, 2000000, 3000000, 4000000, 5000000],
        "expected_prefix": [1000000, 3000000, 6000000, 10000000, 15000000]
    },
    {
        "nums": [2, 2, 2, 2, 2],
        "expected_prefix": [2, 4, 6, 8, 10]
    }
]

for test_case in test_cases:
    nums = test_case["nums"]
    expected_prefix = test_case["expected_prefix"]

    # Compute the prefix sum
    result_prefix = prefix_sum(nums)

    # Check if the computed prefix sum matches the expected result
    if result_prefix == expected_prefix:
        print(f"Test passed: Input: {nums}, Expected Prefix Sum: {expected_prefix}, Computed Prefix Sum: {result_prefix}")
    else:
        print(f"Test failed: Input: {nums}, Expected Prefix Sum: {expected_prefix}, Computed Prefix Sum: {result_prefix}")

    # result_prefix = running_sum(nums)
    # if result_prefix == expected_prefix:
    #     print(f"Test passed: Input: {nums}, Expected Running Sum: {expected_prefix}, Computed Running Sum: {result_prefix}")
    # else:
    #     print(f"Test failed: Input: {nums}, Expected Running Sum: {expected_prefix}, Computed Running Sum: {result_prefix}")
