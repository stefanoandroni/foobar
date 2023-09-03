def solution(banana_list):
    S = get_possible_pairs_leading_to_infinite_loop(banana_list)
    # ...
    
    print(S)
    print(len(S))
    print(len(banana_list))
    return

def get_possible_pairs_leading_to_infinite_loop(L):
    S = set()

    for i in L:
        for j in L:
            if leads_to_infinite_loop(i, j):
                S.add((i, j))
    
    return S

def leads_to_infinite_loop(x, y):
    # y / x = 2 ^ (n + 1) - 1    y > x,  n in N U {0}    =>    return false    else    return true
    
    if x > y:
        x, y = y, x

    r = y % x
    if r != 0:
        return True
    
    q = y//x
    q += 1
    if q & (q-1) == 0: # Check if q is a power of 2 (using bit manipulations) 
        return False
    
    return True

def main():
    assert leads_to_infinite_loop(1, 19) == True
    assert leads_to_infinite_loop(1, 13) == True
    assert leads_to_infinite_loop(1, 21) == True
    assert leads_to_infinite_loop(1, 3) == False
    assert leads_to_infinite_loop(1, 7) == False
    assert leads_to_infinite_loop(5, 14) == True
    assert leads_to_infinite_loop(5, 15) == False
    assert leads_to_infinite_loop(5, 35) == False

    solution([1, 7, 3, 21, 13, 19])

if __name__ == "__main__":
    main()