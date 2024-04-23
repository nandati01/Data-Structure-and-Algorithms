def repeated_characters(s):
    """
    Given a string s
    Return the first character to appear twice
    The time complexity needs to be O(n)
    """
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)
    return ""

s = "abcdeda"
print(repeated_characters(s))
