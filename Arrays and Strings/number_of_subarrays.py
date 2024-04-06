def numof_subarray(nums, k):
    '''
    Given an array of positive integers nums and a constraint k
    Find number of subarrays where product of all the numbers within it is less than k
    '''
    #if k <= 1, we can not have valid windows
    if k <= 1:
        return 0
    
    left = 0
    ans = 0
    window = 1

    for right in range(len(nums)):
        window *= nums[right]
        while window >= k:
            curr //=nums[left]
            left += 1

        ans += right - left + 1

    return ans

test_cases = [
    ([1, 2, 3], 0, 0),       
    ([1, 2, 3], 7, 6),       
    ([4, 1, 2], 10, 6),      
    ([10, 5, 2, 6], 1000, 10), 
    ([], 10, 0),             
    ([1, 1, 1], 2, 6),       
]

for i, (nums, k, expected) in enumerate(test_cases, 1):
    result = numof_subarray(nums, k)
    assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
    print(f"Test case {i} passed.")
