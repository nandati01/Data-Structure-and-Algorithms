def max_vowels(s, k):
    """
    Given a string s and an integer k
    Return the max no. of vowels in any substring of s with length k
    """
    #if the string is empty or k is 0 or larger than the length of s
    if not s or k == 0 or k > len(s):
        return 0
    #initializing the count of vowels
    vowels = 'aeiou'
    count = 0
    #initialize the window and count the no of vowels in the first window
    for i in range(k):
        if s[i] in vowels:
            count += 1
    max_count = count
    #Slide the window across the length of s
    for i in range(k, len(s)):
        if s[i -k] in vowels:
            count -= 1
        if s[i] in vowels:
            count += 1
        max_count = max(max_count, count)
    return max_count

test_cases = [
    ("abcde", 2),  # Basic test
    ("aeiou", 3),  # All vowels
    ("xyz", 3),    # No vowels
    ("aaaae", 2),  # All same vowels
    ("bncmklee", 4),  # Mixed with maximum at the end
    ("", 3),       # Empty string
    ("uoiea", 10)  # k larger than the length of the string
]

for s, k in test_cases:
    result = max_vowels(s, k)
    print(f"Max vowels in {s} with length {k} is {result}")
