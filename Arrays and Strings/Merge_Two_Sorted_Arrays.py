# # Merge Two Sorted Arrays
# 
# Given two sorted integer arrays, return a new sorted array that combines the both of them. Example: arr1 = [1, 3, 5, 7], arr2 = [2, 4, 6, 8, 9], return [1, 2, 3, 4, 5, 6, 7, 8, 9]. 
# 
# To solve this problem, we can use the two pointers method. We will initially set the two pointers to the first index of the two arrays, respectively. The idea is to iteratively compare the elements that each pointer refers to, and selecting the smaller of the two to add to the new array.
# 
# Here's a solution breakdown:
# - Initialize 'i' and 'j' at the beginning of arr1 and arr2 respectively
# - Compare elements at i and j and insert the smaller of the two into a new array 'arr'
# - Increment the pointer that pointed to the smaller array
# - Once one of the pointers reaches the end of its array, append the remaining elements of the other array to arr
# - Return the merged array
# 
# Since the arrays are already sorted, the time complexity for this algorithm is O(n + m)

# %%
def combine(arr1, arr2):
    i = j = 0
    arr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1

    return arr

# %%
test_cases = [
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
    ([1, 3, 5, 7, 9], [2, 4], [1, 2, 3, 4, 5, 7, 9]),
    ([-5, -3, -1], [-4, -2, 0], [-5, -4, -3, -2, -1, 0]),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([], [1, 2, 3], [1, 2, 3]),
    ([], [], []),
    ([1, 3, 5, 7], [3, 5, 7, 9], [1, 3, 3, 5, 5, 7, 7, 9]),
    ([2, 2, 2], [2, 2, 2], [2, 2, 2, 2, 2, 2]),
]

results = []

for arr1, arr2, expected in test_cases:
    result = combine(arr1, arr2)
    success = result == expected
    results.append((result, success))

results


