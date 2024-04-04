# Given an integer array nums sorted in an ascending order
# Return an array of the squares of each number sorted in ascending order using two pointers

#We could simply use sorted(i **2 for i in nums) but it will have a complexity of O(nlogn)

def sortedSquares(nums):
    '''
    Given: a list of numbers in ascending order
    Requirement: Square the numbers and sort it with a complexity of O(n)
    '''

    #Initializing two pointers: one at the first and the other at the last index
    i, j = 0, len(nums) - 1

    #Create a new array to hold the squared numbers
    sorted_squares = [0]*len(nums)

    #To start filling the new array from the end
    k = len(nums)-1

    while i <= j:
        if nums[i]**2 > nums[j]**2:
            sorted_squares[k] = nums[i]**2
            i +=1
        else:
            sorted_squares[k] = nums[j]**2
            j -=1
        k -=1
    return sorted_squares

# Test cases
test_cases = [
    ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]),
    ([-4, -3, -2, -1], [1, 4, 9, 16]),
    ([-5, -3, 0, 2, 4], [0, 4, 9, 16, 25]),
    ([2], [4]),
    ([], []),
    ([0, 0, 0], [0, 0, 0]),
    ([-1000, 500, 1000], [250000, 1000000, 1000000]),
    ([-2, -2, 2, 2], [4, 4, 4, 4])
]

for idx, (input, expected) in enumerate(test_cases, 1):
    result = sortedSquares(input)
    assert result == expected, f"Test case {idx} failed: expected {expected}, got {result}"
    print(f"Test case {idx} passed: got {result}")
    