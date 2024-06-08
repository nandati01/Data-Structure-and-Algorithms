def is_path_crossing(path):
    """
    Given a string path
    path[i] = 'N', 'S', 'E', 'W', each representing north, south,
    east, or west, respectively
    Start at origin (0, 0) on a 2D plane
    Return True if the path crosses itself at any point
    Return False otherwise
    """
    x = y = 0
    visited = set()
    visited.add((x, y))
    moves = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
    for i in path:
        dx, dy = moves[i]
        x += dx
        y += dy

        if (x, y) in visited:
            return True
        visited.add((x, y))
    return False

def test_is_path_crossing():
    # Test case 1: Path crosses itself
    path1 = "NESW"
    assert is_path_crossing(path1) == True, f"Failed for path {path1}"

    # Test case 2: Path does not cross itself
    path2 = "NES"
    assert is_path_crossing(path2) == False, f"Failed for path {path2}"

    # Test case 3: Path crosses itself immediately
    path3 = "NN"
    assert is_path_crossing(path3) == False, f"Failed for path {path3}"

    # Test case 4: Path does not cross itself
    path4 = "ENWS"
    assert is_path_crossing(path4) == True, f"Failed for path {path4}"

    # Test case 5: Empty path
    path5 = ""
    assert is_path_crossing(path5) == False, f"Failed for path {path5}"

    # Test case 6: Path crosses itself in a loop
    path6 = "NESWNESW"
    assert is_path_crossing(path6) == True, f"Failed for path {path6}"

    # Test case 7: Long path without crossing
    path7 = "N" * 100 + "S" * 100 + "E" * 100 + "W" * 100
    assert is_path_crossing(path7) == True, f"Failed for path {path7}"

    # Test case 8: Long path with crossing
    path8 = "N" * 50 + "E" * 50 + "S" * 50 + "W" * 50 + "N" * 25 + "E" * 25 + "S" * 25 + "W" * 25
    assert is_path_crossing(path8) == True, f"Failed for path {path8}"

    print("All test cases pass")

# Run the test cases
test_is_path_crossing()
