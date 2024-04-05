def longest_substring(s):
    """
    Given: a binary string s
    You are allowed to flip only one "0" to a "1"
    Find the longest length of a substring that contains only "1"
    """

    left = 0
    #zero_count is the number of "0"s in the window
    #The idea is to shrink the window from left if zero_count > 1
    zero_count = 0
    ans = 0

    for right in range(len(s)):
        if s[right] == "0":
            zero_count += 1
        while zero_count> 1:
            if s[left] == "0":
                zero_count -= 1
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans

test_cases = [
    "110101110",
    "11111",
    "0000",
    "10001",
    "0110101",
]
for i, test_case in enumerate(test_cases):
    result = longest_substring(test_case)
    print(f"Test case {i + 1}: '{test_case}' -> Longest Substring Length: {result}")
    