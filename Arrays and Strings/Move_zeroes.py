def move_zeroes(nums):
    """
    Given an integer array nums
    Move all 0's to the end
    Also maintain the original order of the non-zero elements
    """
    insert_pos = 0
    for num in nums:
        if num != 0:
            #Inserting non-zero elements to the beginning of nums
            nums[insert_pos] = num
            insert_pos += 1
    #filling the rest of the array with zeroes
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1
    return nums

test_cases = [
        [0, 1, 0, 3, 12],
        [0, 0, 0, 0, 0],
        [1, 2, 3, 4, 5],
        [0, 0, 1, 0],
        [1],
        [1, 0],
        [0, 1]
    ]
for i, nums in enumerate(test_cases, 1):
    print(f"Input {i}: {nums} -> Output: {move_zeroes(nums)}")
