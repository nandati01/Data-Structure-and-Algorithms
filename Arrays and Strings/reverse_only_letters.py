def reverse_only_letters(s):
    """
    Given a string s
    Reverse all letters
    But keep the original position of characters that are not letters
    """
    s_list = list(s)
    left = 0
    right = len(s_list) - 1
    while left < right:
        if not s_list[left].isalpha():
            left += 1
        elif not s_list[right].isalpha():
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    return "".join(s_list)

test_cases = [
        ("ab-cd", "dc-ba"),
        ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
        ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),
        ("", ""),
        ("123$%^", "123$%^"),
        ("a", "a"),
        ("-a-", "-a-"),
        ("Z<*zj", "j<*zZ"),
        ("--ab--", "--ba--"),
        ("ABCdef", "fedCBA"),
        ("aA1bB2", "Bb1Aa2"),
        ("TestCasesAreFun!", "nuFerAsesaCtseT!"),
        ("OnlyLetters", "sretteLylnO"),
        ("With3Numbers123", "sreb3muNhtiW123"),
        ("Special$$$Chars", "srahCla$$$icepS"),
        ("CAPSandlower", "rewoldnaSPAC"),
        ("--++--abCD", "--++--DCba"),
        ("Mixed-123-With-Letters", "srett-123-eLht-iWdexiM"),
        ("Palindrome-emordnilaP", "Palindrome-emordnilaP"),
        ("NoLettersHere!", "ereHsretteLoN!"),
        ("EndsWithALetterr", "rretteLAhtiWsdnE")
    ]

for i, (input_str, expected) in enumerate(test_cases, 1):
    result = reverse_only_letters(input_str)
    assert result == expected, f"Test Case {i}: Expected {expected}, got {result} for input {input_str}"
    print(f"Test Case {i}: Passed, Input: {input_str}, Result: {result}")
