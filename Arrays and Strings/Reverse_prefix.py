def reverse_prefix(word, ch):
    """
    Given a string word and a character ch
    Reverse the segment of word that starts at index 0
    and ends at the index of the first occurrrence of ch (inculsive)
    """
    try: #This will raise value error if ch is not found
        right = word.index(ch)
        left = 0
        lst = list(word) #convert into list to make it mutable
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        return "".join(lst)
    except ValueError:
        return word

def test_reverse_prefix():
    # Test case 1: Character is found and is in the middle of the word
    assert reverse_prefix("abcdefd", "d") == "dcbaefd", "Test Case 1 Failed"

    # Test case 2: Character is not found
    assert reverse_prefix("hello", "z") == "hello", "Test Case 2 Failed"

    # Test case 3: Character is at the beginning of the word
    assert reverse_prefix("example", "e") == "example", "Test Case 3 Failed"

    # Test case 4: Character is at the end of the word
    assert reverse_prefix("abcxyz", "z") == "zyxcba", "Test Case 4 Failed"

    # Test case 5: Single character word, character found
    assert reverse_prefix("a", "a") == "a", "Test Case 5 Failed"

    # Test case 6: Single character word, character not found
    assert reverse_prefix("a", "b") == "a", "Test Case 6 Failed"

    # Test case 7: Empty string
    assert reverse_prefix("", "x") == "", "Test Case 7 Failed"

    print("All test cases passed!")

# Running the tests
test_reverse_prefix()
