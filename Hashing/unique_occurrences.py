def unique_occurrences(arr):
    """
    Given an array of integers arr
    Return True if the no of occurrences of each value in arr is unique
    False otherwise
    """
    dic = {i: arr.count(i) for i in arr}
    return len(set(dic.values())) == len(dic.values())

def test_unique_occurrences():
    # Test Case 1: Simple case with unique occurrences
    assert unique_occurrences([1, 2, 2, 1, 1, 3]) == True, "Test Case 1 Failed"   
    # Test Case 2: Simple case without unique occurrences
    assert unique_occurrences([1, 2, 2, 1, 3, 3]) == False, "Test Case 2 Failed"
    # Test Case 3: Empty array
    assert unique_occurrences([]) == True, "Test Case 3 Failed"
    # Test Case 4: Single element array
    assert unique_occurrences([5]) == True, "Test Case 4 Failed"
    # Test Case 5: All elements are the same
    assert unique_occurrences([7, 7, 7, 7, 7]) == True, "Test Case 5 Failed"
    # Test Case 6: Multiple elements, all unique
    assert unique_occurrences([1, 2, 3, 4, 5]) == False, "Test Case 6 Failed"
    # Test Case 7: Large array with unique occurrences
    assert unique_occurrences([1]*10 + [2]*20 + [3]*30 + [4]*40) == True, "Test Case 7 Failed"
    # Test Case 8: Large array without unique occurrences
    assert unique_occurrences([1]*10 + [2]*20 + [3]*30 + [4]*30) == False, "Test Case 8 Failed"
    # Test Case 9: Mixed positive and negative numbers with unique occurrences
    assert unique_occurrences([-1, -1, -2, -2, -3, -3, -3]) == False, "Test Case 9 Failed"
    # Test Case 10: Mixed positive and negative numbers without unique occurrences
    assert unique_occurrences([-1, -1, -2, -2, -3, -3, -3, -3]) == False, "Test Case 10 Failed"
    print("All test cases pass")

# Run the test cases
test_unique_occurrences()
