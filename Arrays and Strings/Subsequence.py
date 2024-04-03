# Given two strings s1 and s2, return True is s1 is a subsequence of s2
# For example: s1 = "abc" s2 = "ahbgdc"; s1 is a subsequence of s2
# If s1 = "agh", s2 = "ahbgdc"; s1 is not a subsequence of s2

def is_subsequence(s1, s2):
    # Initialize two pointers to the first characters of the two strings
    i = j = 0

    while i < len(s1) and j < len(s2):
        #Check if all characters in s1 are found
        if s1[i] == s2[j]:
            i += 1
        #Iterate through each character in s2
        j += 1

    #If pointer i equals the length of s1, all characters are found in sequence
    return i == len(s1)

# Now, let's create some test cases to check if the function works as expected
test_cases = [
    ("abc", "ahbgdc", True),  # Should return True
    ("agh", "ahbgdc", False),  # Should return False
    ("", "ahbgdc", True),  # An empty string is a subsequence of any string
    ("abcd", "abcd", True),  # Identical strings
    ("abcdef", "abc", False),  # s1 is longer than s2, cannot be a subsequence
]

results = []
for s1, s2, expected in test_cases:
    result = is_subsequence(s1, s2)
    results.append((f"s1 = {s1}, s2 = {s2}, Expected: {expected}, Result: {result}"))

print(results)