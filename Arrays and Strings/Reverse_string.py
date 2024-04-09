def reverse_string(s):
    """Given a string s 
    Reverse the string preserving the white space of the initial word
    For example: s = 'Hello World'
    return olleH dlroW
    """
    words = list(s.split(" "))
    reverse = [word[::-1] for word in words]
    return " ".join(reverse)

test_cases = [
        "example string with spaces",
        "single",
        "with   multiple   spaces",
        "Mr Ding",
        "",
        "punctuation, here!"
    ]
ans = [reverse_string(test) for test in test_cases]
print(ans)
