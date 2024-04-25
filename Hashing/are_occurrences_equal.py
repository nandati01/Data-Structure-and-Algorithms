from collections import defaultdict

def are_occurrences_equal(s):
    """
    Given a string s 
    Determine if all the characters have the same frequency
    For example: s = "abacbc", return True
    s = "aaabb", return False
    """
    count = defaultdict(int)
    for c in s:
        count[c] += 1
    
    frequencies = count.values()
    return len(set(frequencies)) == 1

s = "abacbc"
print(are_occurrences_equal(s))
s = "aaabb"
print(are_occurrences_equal(s))
