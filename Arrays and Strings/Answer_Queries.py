def answer_queries(nums, queries, limit):
    """
    Given: an integer array nums, queries[i] = [x, y], limit
    Return: True if the sum of subarray x to y is less than the limit
    """
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    result = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        result.append(curr < limit)
    
    return result

nums_test = [1, 2, 3, 4, 5]
queries_test = [(0, 2), (1, 3), (0, 4)]
limit_test = 10

test_result = answer_queries(nums_test, queries_test, limit_test)
print(test_result)

nums_test = [1, 6, 3, 2, 7, 2]
queries_test = [[0, 3], [2, 5], [2, 4]]
limit_test = 13
test_result = answer_queries(nums_test, queries_test, limit_test)
print(test_result)
