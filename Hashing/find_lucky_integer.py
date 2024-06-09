from collections import defaultdict
def find_lucky(arr):
    """
    Given an integer arr, a lucky integer has a frequency in the arr equal to its value
    Return the largest lucky integer in the arr
    If there is no lucky number return -1
    """
    count = defaultdict(int)
    ans = -1
    for num in arr:
        count[num] += 1
    for k, v in count.items():
        if k == v:
            ans = max(ans, v)
    return ans

def test_find_lucky():
    # Test case 1: Typical case with a lucky number
    arr1 = [2, 2, 3, 3, 3]
    assert find_lucky(arr1) == 3, f"Test case 1 failed, expected 3 but got {find_lucky(arr1)}"

    # Test case 2: No lucky number
    arr2 = [2, 2, 3, 3, 4, 4, 4, 4]
    assert find_lucky(arr2) == 4, f"Test case 2 failed, expected 4 but got {find_lucky(arr2)}"

    # Test case 3: Multiple lucky numbers
    arr3 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    assert find_lucky(arr3) == 4, f"Test case 3 failed, expected 4 but got {find_lucky(arr3)}"

    # Test case 4: All elements are lucky
    arr4 = [1, 2, 2, 3, 3, 3]
    assert find_lucky(arr4) == 3, f"Test case 4 failed, expected 3 but got {find_lucky(arr4)}"

    # Test case 5: Single element array (lucky number)
    arr5 = [1]
    assert find_lucky(arr5) == 1, f"Test case 5 failed, expected 1 but got {find_lucky(arr5)}"

    # Test case 6: Single element array (not lucky)
    arr6 = [2]
    assert find_lucky(arr6) == -1, f"Test case 6 failed, expected -1 but got {find_lucky(arr6)}"

    # Test case 7: Large numbers
    arr7 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert find_lucky(arr7) == 10, f"Test case 7 failed, expected 10 but got {find_lucky(arr7)}"

    print("All test cases passed!")

# Run the test cases
test_find_lucky()
