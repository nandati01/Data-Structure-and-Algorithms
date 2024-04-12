def highest_altitude(gain):
    """
    Given an integer array gain
    Return the highest altitude
    """
    prefix = [0]
    for i, height in enumerate(gain):
        prefix.append(height + prefix[-1])
    return max(prefix)

test_cases = [
    ([-5, 1, 5, 0, -7], 1),
    ([-4, -3, -2, -1, 4, 3, 2], 0),
    ([10, -3, -4, 7, 0, 5, -2], 15),
    ([0, 0, 0, 0], 0),
    ([1, 2, 3, 4, 5], 15),
    ([-1, -1, -1, -1], 0),
    ([], 0)  # Edge case: empty gain array, should technically never be zero, might adjust function to handle it
]
for i, (gain, expected) in enumerate(test_cases):
    result = highest_altitude(gain)
    print(f"Test Case {i}: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")
    