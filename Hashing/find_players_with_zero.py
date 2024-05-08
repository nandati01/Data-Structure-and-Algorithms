from collections import defaultdict
def find_winners(matches):
    """Given an integer array matches
    matches[i] = [winner_i, loser_i] indicating winner_i defeated loser_i
    Return a list of size 2 where:
        answer[0] = list of players with 0 losses
        answer[1] = list of players with only 1 losses
    """

    wins = defaultdict(int)
    losses = defaultdict(int)
    for match in matches:
        wins[match[0]] += 1
        losses[match[1]] += 1
    return [[k for k in wins.keys() if k not in losses.keys()], [k for k in losses.keys() if losses[k] == 1]]
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(find_winners(matches))
matches = [[2,3],[1,3],[5,4],[6,4]]
print(find_winners(matches))
