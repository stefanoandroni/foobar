# admitted operations: [:2], [+1], [-1]

# Note
#   > [:2] always better then [+1] or [-1] (so if possible (even number), choose this one)
#   > [+1] and [-1] make an odd number even, but if n%4=3, adding 1 (n%4=0) is a better choice because it makes it doubly divisible


def solution(n):
    n = int(n)

    count = 0
    while n >= 4:
        if n & 1:  # n is odd (...1)
            if n & 2:  # n%4=3 (...11)
                n = (n + 1) >> 2  # [+1] [:2] [:2]
                count += 3
            else:
                n = (n - 1) >> 1  # [-1] [:2]
                count += 2
        else:  # n is even (...0)
            n = n >> 1  # [:2]
            count += 1

    if n == 3:
        n -= 1  # [-1]
        count += 1

    if n == 2:
        n -= 1  # [-1]
        count += 1

    return count


def main():
    assert(solution("4") == 2)
    assert(solution("15") == 5)


if __name__ == "__main__":
    main()
