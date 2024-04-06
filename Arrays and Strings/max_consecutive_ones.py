def longest_ones(nums, k):
    """Given a binary array nums and an integer k
    return the maximum number of consecutive ones 
    you can flip at most k ones
    """
    zero_count = left = 0
    ans = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

tests = [
    ([1, 1, 0, 0, 1, 1, 1, 0, 1, 1], 2),   # Mixed zeros and ones, k=2
    ([0, 0, 1, 1, 0, 0, 1, 1, 0], 2),      # Mixed zeros and ones, k=2
    ([1, 1, 1, 1, 1], 2),                  # All ones, k=2
    ([0, 0, 0, 0], 2),                     # All zeros, k=2
    ([1, 0, 1, 0, 1], 1),                  # Alternating ones and zeros, k=1
    ([], 2),                               # Empty array, k=2
    ([0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1], 3) # Mixed, with higher k=3
]

for (nums, k) in tests:
    print(f"nums: {nums}, k: {k} -> {longest_ones(nums, k)}")
    