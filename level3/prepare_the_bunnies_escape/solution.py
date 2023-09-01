# TODO: optimization also in w ?


def solution(map):  # BFS
    # state -> (row:int, col:int, wall:boolean, pathLength:int)
    global H, W, BS  # H: matrix height, W: matrix width, BS: best states [key: (r,c,w), value: l]

    H, W = get_map_size(map)

    BS = {}
    queue = []

    s0 = (0, 0, True, 1)
    queue.append(s0)

    while queue:
        r, c, w, l = queue.pop(0)
        if (r == H - 1 and c == W - 1):  # End Cell (BFS ensures that the first path found is the best)
            return l
        possible_states = get_possible_states(map, (r, c, w, l))
        opt_states = get_opt_states(possible_states)
        for s in opt_states:
            queue.append(s)


def get_opt_states(states):
    opt_states = []
    for r, c, w, l in states:
        if (r, c, w) in BS:
            if BS[(r, c, w)] > l:
                opt_states.append((r, c, w, l))
                BS[(r, c, w)] = l  # update state in BS
        else:
            opt_states.append((r, c, w, l))
            BS[(r, c, w)] = l  # add state to BS
    return opt_states


def get_possible_states(map, s):
    r, c, w, l = s
    possible_states = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dr, dc in dirs:
        nr, nc = (r + dr, c + dc)
        # Check if in matrix limits
        if (0 <= nr <= H - 1) and (0 <= nc <= W - 1):
            # Check if there is a wall
            if map[nr][nc] == 1:
                # Check if it can still remove a wall
                if w:
                    possible_states.append((nr, nc, False, l + 1))
            else:
                possible_states.append((nr, nc, w, l + 1))
    return possible_states


def get_map_size(map):
    return len(map), len(map[0])


def main():
    assert(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 11)
    assert(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) == 7)


if __name__ == "__main__":
    main()
