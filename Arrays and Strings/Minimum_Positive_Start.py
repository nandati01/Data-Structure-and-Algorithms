def min_start_value(nums):
    """
    Given an array of integers nums
    Start with an initial positive value startValue
    In each iteration calculate the step by step of startValue + elements in num
    Return the minimum positive value of srartValue 
    such that the step by step sum is never less than 1
    """
    min_sum = 0
    running_sum = 0

    for num in nums:
        running_sum += num
        min_sum = min(min_sum, running_sum)
    #To make sure the step by step never drops below 1, we do 1 - min_sum
    #Since minsum will be 0 or negative in such cases and we need to offset it to start at 1
    #If minsum is 1 or greater, then startValue can be 1
    #Since we never drop below 1
    return max(1, 1-min_sum)

test_cases = [
    [-3, 2, -3, 4, 2], # Example 1: Minimum start value should be 5
    [1, 2], # Example 2: Minimum start value should be 1 (since we never go below 1)
    [1, -2, -3] # Example 3: Minimum start value should be 5
]

print([min_start_value(tc) for tc in test_cases])
