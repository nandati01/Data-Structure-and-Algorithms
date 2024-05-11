from collections import defaultdict
def len_of_substring(s):
    """
    Given a string s
    Return the length of the longest substring without repeating any characters
    """
    counts = defaultdict(int)
    left = ans = 0
    for right, c in enumerate(s):
        counts[c] += 1
        while counts[c] > 1:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        ans = max(ans, right - left + 1)
    return ans
test_strings = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
    "",
    "a",
    "abcdef",
    "abc123!@#",
    "abba",
    "abcbdef",
    "aaaaaaab"
]

for test in test_strings:
    print(f"Input: {test}, Output: {len_of_substring(test)}")
