def count_elements(arr):
    """
    Given an array with integers
    Count how many elements x there are
    Such that x + 1 is also in arr
    """
    count = 0
    for x in arr:
        if x + 1 in arr:
            count += 1
    return count

    #An alternative way
    # dic = {}
    # for i, x in enumerate(arr):
    #     if x not in dic:
    #         dic[x] = [i]
    #     else:
    #         dic[x].append(i)
    # new = []
    # for i in arr:
    #     if i + 1 in dic:
    #         new.append(i)
    # return len(new)
arr = [1,2,3]
print(count_elements(arr))
arr = [1,1,3,3,5,5,7,7]
print(count_elements(arr))
