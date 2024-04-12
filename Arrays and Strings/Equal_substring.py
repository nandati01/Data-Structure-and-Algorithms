def equal_substring(s, t, maxCost):
    """
    Given two strings s and t and an integer maxCost
    We want to s[i] to t[i]
    Cost of changing s to t is |s[i] - t[i]|
    Return maximum length of a substring of s
    that can be changed to be the  same as the correspoinding substring of t
    with a cost less than or equal to maxCost
    """
    #cost of changing the ith character of s to the ith character of t
    cost = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
    #initializing the sliding window
    left = total_cost = max_length = 0

    for right in range(len(s)):
        total_cost += cost[right]
        while total_cost > maxCost:
            total_cost -= cost[left]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

def test_equalSubstring():
    # Basic test cases from the examples provided
    assert equal_substring("abcd", "bcdf", 3) == 3, "Test case 1 failed"
    assert equal_substring("abcd", "cdef", 3) == 1, "Test case 2 failed"
    assert equal_substring("abcd", "acde", 0) == 1, "Test case 3 failed"
    # Boundary cases
    # Case where no change is needed
    assert equal_substring("aaaa", "aaaa", 5) == 4, "Test case 4 failed"
    # Case where each change is very costly
    assert equal_substring("aaaa", "bbbb", 1) == 1, "Test case 5 failed"
    # Case with empty strings
    assert equal_substring("", "", 10) == 0, "Test case 6 failed"
    # Case where only the max length substring has a cost at the limit
    assert equal_substring("xyz", "abc", 42) == 1, "Test case 7 failed"
    # Large cost allowance
    assert equal_substring("xyz", "abc", 100) == 3, "Test case 8 failed"
    # No cost allowance and different strings
    assert equal_substring("xyz", "abc", 0) == 0, "Test case 9 failed"
    # Testing single character cost limits
    assert equal_substring("z", "a", 25) == 1, "Test case 10 failed"
    assert equal_substring("z", "a", 26) == 1, "Test case 11 failed"

    print("All test cases passed!")

test_equalSubstring()
