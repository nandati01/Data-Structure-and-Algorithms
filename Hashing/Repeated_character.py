def repeated_characters(s):
    """
    Given a string s
    Return the first character to appear twice
    """
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)
    return ""

s = "abcdeda"
print(repeated_characters(s))
