def solution(*args):
    banana_list = args[0] if len(args) == 1 else [arg for arg in args]

    E = get_possible_pairs_leading_to_infinite_loop(banana_list)  # E: set of all possible pairs leading to an infinite loop
    MCM = get_maximum_cardinality_matching(E)  # MCM: maximum cardinality matching

    return len(banana_list) - 2 * MCM


def get_maximum_cardinality_matching(S):
    # (?) blossom algorithm (maximum cardinality matching (maximum independent edge set))
    # (X) greedy algorithm
    
    if len(S) == 0:
        return 0

    M = set()  # M: matching

    # Initialize a dictionary to represent the adjacency dict of G=(V,E)
    adjacency_dict = dict()
    for x, y in S:
        if not x in adjacency_dict:
            adjacency_dict[x] = set()
        if not y in adjacency_dict:
            adjacency_dict[y] = set()

        adjacency_dict[x].add(y)
        adjacency_dict[y].add(x)

    # <bad code>
    sorted_keys = sorted(adjacency_dict.keys(), key=lambda k: len(adjacency_dict[k]))

    while len(sorted_keys) > 1:
        sorted_keys = sorted(sorted_keys, key=lambda k: len(adjacency_dict[k]))
        key = sorted_keys[0]

        sorted_values = sorted(adjacency_dict[key], key=lambda value: len(adjacency_dict[value]))

        if len(sorted_values) > 0:
            chosen_value = sorted_values[0]

            M.add((key, chosen_value))
            adjacency_dict.pop(key)
            adjacency_dict.pop(chosen_value)
            for k in adjacency_dict:
                adjacency_dict[k].discard(chosen_value)
                adjacency_dict[k].discard(key)
            sorted_keys.remove(chosen_value)

        sorted_keys.remove(key)
    # </bad code>

    return len(M)


def get_possible_pairs_leading_to_infinite_loop(L):
    # (use indices, to handle the case of multiple trainers with the same number of bananas)
    P = [(ida, idb + ida + 1) for ida, a in enumerate(L) for idb, b in enumerate(L[ida + 1 :]) if lead_to_infinite_loop(a, b)]
    return P


def lead_to_infinite_loop(x, y):
    """
    Checks if x and y lead to an infinite loop, ie iff   with y >= x    y / x != 2 ^ (n + 1) - 1    for any n belong to N U {0}

    Parameters:
        x (int): Element 1.
        y (int): Element 2.

    Returns:
        bool: True if it leads to an infinite loop, False otherwise.
    """

    # Ensure that y >= x
    if x > y:
        x, y = y, x

    # If the remainder of y / x division is not zero, the equation cannot be
    # satisfied for any value of n (x and y lead to an infinte loop)
    r = y % x
    if r != 0:
        return True

    # If (y / x) + 1 is a power of 2, the equation can be satisfied for a value
    # of n (x and y do not lead to an infinte loop)
    q = y // x
    q += 1
    if q & (q - 1) == 0:  # Check if q is a power of 2 (using bit manipulations)
        return False
    else:
        return True


def main():
    assert lead_to_infinite_loop(7, 7) == False
    assert lead_to_infinite_loop(1, 19) == True
    assert lead_to_infinite_loop(1, 13) == True
    assert lead_to_infinite_loop(1, 21) == True
    assert lead_to_infinite_loop(1, 3) == False
    assert lead_to_infinite_loop(1, 7) == False
    assert lead_to_infinite_loop(5, 14) == True
    assert lead_to_infinite_loop(5, 15) == False
    assert lead_to_infinite_loop(5, 35) == False

    assert solution([1, 7, 3, 21, 13, 19]) == 0
    assert solution([1, 1]) == 2
    assert solution(1, 1) == 2
    assert solution([3, 3, 2, 6, 6]) == 1
    assert solution([1, 7, 21]) == 1
    assert solution(1, 2) == 0


if __name__ == "__main__":
    main()