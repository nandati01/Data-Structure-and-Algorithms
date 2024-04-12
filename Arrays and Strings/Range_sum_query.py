class NumArray:
    # The constructor takes an array of integers as an input.
    def __init__(self, nums):
        self.n = len(nums)
        self.prefix = [0] * self.n
        # Handle edge case where nums could be empty to prevent index errors.
        if nums:
            self.prefix[0] = nums[0]
            # Compute the prefix sum array
            for i in range(1, self.n):
                self.prefix[i] = self.prefix[i - 1] + nums[i]

    # This function returns the sum of the elements between indices left and right (inclusive).
    def sumRange(self, left: int, right: int) -> int:
        # If the left index is 0, return the prefix sum at the right index directly.
        if left == 0:
            return self.prefix[right]
        else:
            # Otherwise, calculate the sum as the difference between the prefix sum at the right index
            # and the prefix sum just before the left index.
            return self.prefix[right] - self.prefix[left - 1]
test_cases = [
    {
        "nums": [-2, 0, 3, -5, 2, -1],
        "queries": [(0, 2), (2, 5), (0, 5)],
        "expected": [1, -1, -3]
    },
    {
        "nums": [1, 2, 3, 4, 5],
        "queries": [(1, 3), (0, 4)],
        "expected": [9, 15]
    }
]

# Function to run test cases
def run_test_cases(test_cases):
    results = []
    for case in test_cases:
        obj = NumArray(case["nums"])
        result = []
        for left, right in case["queries"]:
            result.append(obj.sumRange(left, right))
        results.append(result == case["expected"])
    return results

# Execute the test cases
print(run_test_cases(test_cases))
