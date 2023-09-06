from itertools import combinations as comb # emitted in lexicographic ordering according to the order of the input iterable


def solution(num_buns, num_required):
    n = num_buns - (num_required - 1)  # n: copies for each key
    c = comb(range(num_buns), n)  # c: all possible [r] length subsequences of elements from the input [i] 

    # Initialize the 'out' list with empty lists for each bunny
    out = [[] for _ in range(num_buns)]
    # Iterate through the combinations [c] and assign keys [k] to bunnies [b]
    for k, bunnies in enumerate(c):
        for b in bunnies:
            out[b].append(k)

    return out


def main():
    assert (solution(5, 3)) == [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]]
    assert (solution(2, 1)) == [[0], [0]]
    assert (solution(4, 4)) == [[0], [1], [2], [3]]
    assert (solution(3, 1)) == [[0], [0], [0]]
    assert (solution(2, 2)) == [[0], [1]]
    assert (solution(3, 2)) == [[0, 1], [0, 2], [1, 2]]


if __name__ == "__main__":
    main()
