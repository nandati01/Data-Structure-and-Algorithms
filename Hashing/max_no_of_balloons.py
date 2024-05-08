from collections import defaultdict
def max_balloons(text):
    """
    Given a string text
    Find the number of times the word "balloon" appears
    You can only use each character in text at most once
    """
    count = defaultdict(int)
    for letter in text:
        if letter in "balloon":
            count[letter] += 1
    return min(count['b'], count['a'], count['l'] // 2, count['o'] // 2, count['n'])
text = "nlaebolko"
print(max_balloons(text))
text = "loonbalxballpoon"
print(max_balloons(text))
