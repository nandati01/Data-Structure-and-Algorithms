def dest_city(paths):
    """
    Given the array paths
    paths[i] = [cityA, cityB], means there exists a direct path from A to B
    Return destination city, that is the city without any path 
    outgoing to another city
    """
    origin = {path[0] for path in paths}
    for path in paths:
        if path[1] not in origin:
            return path[1]

test_cases = [
    {"input": [["A", "B"]], "expected": "B"},                           # Single path
    {"input": [["A", "B"], ["B", "C"], ["C", "D"]], "expected": "D"},   # Multiple paths forming a line
    {"input": [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]], "expected": "Sao Paulo"}, # Real case
    {"input": [["X", "Y"], ["Y", "Z"], ["Z", "A"]], "expected": "A"},   # Circular paths not valid per problem constraints
]

# Run test cases
for case in test_cases:
    result = dest_city(case["input"])
    assert result == case["expected"], f"Test failed for input {case['input']}. Expected {case['expected']}, got {result}"

print("All tests passed!")
