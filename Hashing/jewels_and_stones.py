def num_jewels_in_stones(jewels, stones):
    """
    Given strings jewels representing the types of stones that are jewels
    Given stones representing the stones you have
    Return how many of the stones you have are also jewels
    """
    jewels_set = set(jewels)
    return sum(stone in jewels_set for stone in stones)
print(num_jewels_in_stones(jewels = "aA", stones = "aAAbbbb"))
