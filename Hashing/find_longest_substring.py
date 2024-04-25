#defaultddict provides a default values for keys that haven't been set yet
from collections import defaultdict
def find_longest_substring(s, k):
    """
    Given a string s and an integer k
    Return length of the longest substring that contains at most k distinct chars
    For example: s = "eceba" k = 2, return "ece"
    """
    #Let's consider using a sliding window
    #And use a hash map counts to keep count of the chars in the window
    counts = defaultdict(int) #dictionary with a default value of 0
    left = ans = 0
    for right, c in enumerate(s):
        #Increment the count of char at the right of the window
        counts[c] += 1
        #while the constraint is broken
        while len(counts) > k:
            #start deleting from the left
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        ans = max(ans, right - left + 1)
    return ans

s = "eceba"
k = 2
print(find_longest_substring(s,k))
