def max_sum_subarray(nums, k):
    '''Given an integer array nums, and a fixed window length of k
    Find the sum of subarray with the largest sum 
    '''
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        #if we add i to the window, we need to remove i - k 
        #since the window is of fixed size k
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

test_cases = [
    ([1, 2, 3, 4, 5, 6, 7], 3),
    ([-1, -2, -3, -4, -5, -6, -7], 2),
    ([10, -2, 4, -1, 3, 2, -3, 0], 4),
    ([5, 5, 5, 5, 5], 5),
    ([2, 3, 4, 1, 5], 1)
]

for nums, k in test_cases:
    print(f"Array: {nums}, k: {k} => Max Sum: {max_sum_subarray(nums, k)}")
