from collections import defaultdict
def group_anagrams(strs):
    """
    given an array of strs
    group anagrams together
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    return [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    if n = len(strs) and m is the average len of the strings
    total cost = O(n.m.logm + n)
    """
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)
    return groups.values()
strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))
