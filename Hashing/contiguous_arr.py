def find_max_length(nums):
    """
    given a binary nums
    return max length of a contiguous subarray with an equal no of 0 and 1
    """
    #Transform the array: 0 -> -1, 1 -> 1
    nums = [1 if x == 1 else -1 for x in nums]

    #Hash map to store the first occurrence of each cumulative sum
    #sum_index = {sum:index}
    sum_index = {0:-1} # Initialize with 0 sum at index -1 to handle cases where subarray starts from index 0
    max_length = 0
    curr_sum = 0
    for i, num in enumerate(nums):
        curr_sum += num
        #if the sum has been seen before
        #calculate the length of the subarray
        if curr_sum in sum_index:
            #The length of the current zero sum array
            subarray_length = i - sum_index[curr_sum]
            max_length = max(max_length, subarray_length)
        else:
            #Store the first occurence of this sum
            sum_index[curr_sum] = i
    return max_length
nums = [0,1]
print(find_max_length(nums))
nums = [0,1,0]
print(find_max_length(nums))
nums = [1, 0, 1, 0, 1]
print(find_max_length(nums))
