"""
PROBLEM
    Number of partitions of N into distinct parts (at least two parts).

STATE
    M[i][j]    =>   number of sets of distinct natural numbers <= j which sum to i 

RELATION
    M[i][j]    =    M[i][j-1]       =>  (don't use j)
                        +
                    M[i-j][j-1]     =>  (use j)
                                                   
SOLUTION
    M[N][N-1]   =>  number of sets of distinct natural numbers <= N-1 which sum to N

BASE CASES
        (i)     (j)         M[i][j]
    (1)  0      j       ->  1         
    (2)  i>0    0       ->  0

ALGORITHM
    Bottom-Up approach
"""

def solution(n):
    M = [[0 for i in range(n + 1)] for j in range(n + 1)]
    M[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if (j - 1) <= (i - j):
                M[i][j] = M[i][j - 1] + M[i - j][j - 1]
            else:
                M[i][j] = M[i][j - 1] + M[i - j][i - j]

    return M[n][n - 1]

def main():
    assert(solution(5) == 2)
    assert(solution(200) == 487067745)


if __name__ == "__main__":
    main()