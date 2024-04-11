def get_common(nums1, nums2):
    """
    Given two sorted integers nums1 and nums2
    Return the minimum integer common to both arrays
    for example: nums1 = [1, 2, 3, 4], nums2 = [2, 3, 4], return 2
    """
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] == nums2[j]:
            return nums1[i]
    return -1

test_cases = [
    ([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]),  # Multiple common integers
    ([1, 2, 6, 7, 8], [3, 4, 5, 6, 9]),  # Single common integer
    ([2, 4, 6], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),  # One array is a subset
    ([0, 1, 2, 3], [4, 5, 6]),  # No common integers
    ([], [1, 2, 3]),  # One array is empty
    ([], [])  # Both arrays are empty
]

for nums1, nums2 in test_cases:
    print(f"nums1: {nums1}, nums2: {nums2} => Minimum Common Integer: {get_common(nums1, nums2)}")
