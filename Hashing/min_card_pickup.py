from collections import defaultdict
def min_card_pickup(cards):
    """
    Given an integer array cards
    Return the length of the shortest subarray that contains at least one duplicates
    For example: cards = [1, 2, 6, 2, 1] -> {1: [0, 4], 2: [1, 3], 6: [2]}
    Return 2
    """
    count = defaultdict(list)
    for i, card in enumerate(cards):
        count[card].append(i)

    ans = float("inf")
    for key in count:
        arr = count[key]
        for i in range(len(arr)-1):
            ans = min(ans, arr[i+1] - arr[i]+1)
    return ans if ans < float("inf") else -1
cards = [1, 2, 6, 2, 1]
print(min_card_pickup(cards))
