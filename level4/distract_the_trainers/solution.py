def solution(banana_list):
    E = get_possible_pairs_leading_to_infinite_loop(banana_list) # E: set of all possible pairs leading to an infinite loop
    MCM = get_maximum_cardinality_matching(E) # MCM: maximum cardinality matching (maximum independent edge set) of G=(V,E)
    return len(banana_list) -  2 * MCM

def get_maximum_cardinality_matching(S):
    # (?) blossom algorithm
    return 0

def get_possible_pairs_leading_to_infinite_loop(L):
    S = set()

    for i in L:
        for j in L:
            # ? i and j same item case
            if lead_to_infinite_loop(i, j):
                if j > i:
                    S.add((i, j))
                else:
                    S.add((j, i))

    
    return S

def lead_to_infinite_loop(x, y) -> bool:
    """
    Checks if x and y lead to an infinite loop, ie iff   with y >= x    y / x != 2 ^ (n + 1) - 1    ∀ n ∈ N ∪ {0}
    
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
    q = y//x
    q += 1
    if q & (q-1) == 0: # Check if q is a power of 2 (using bit manipulations) 
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

    # solution([1, 7, 3, 21, 13, 19])

if __name__ == "__main__":
    main()