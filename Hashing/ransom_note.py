from collections import defaultdict
def can_construct(ransomnote, magazine):
    """
    Given two strings ransomnote and magazine
    Return true if ransomnote can be constructed by using the letters from magazine
    False otherwise
    """
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    for s in ransomnote:
        dic1[s] += 1
    for s in magazine:
        dic2[s] += 1
    for k in dic1.keys():
        if dic2.get(k) == None:
            return False
        elif dic2[k] < dic1[k]:
            return False
    return True

test_cases = [
    ("a", "b"),      # Output: False
    ("aa", "ab"),    # Output: False
    ("aa", "aab")    # Output: True
]
for ransomnote, magazine in test_cases:
    print(f"Ransom Note: {ransomnote}, Magazine: {magazine}")
    print("Output:", can_construct(ransomnote, magazine))
    print()
    