def strange_grid():
    pass


def create_infinity_matrix():
    max_col = 5
    max_row = 2*(10**9)
    M = []
    for i in xrange(0, max_row - 1):
        r = []
        for j in xrange(0, max_col - 1):
            r.append(j)
        M.append(r)
    return M


def run():
    print create_infinity_matrix()

if __name__ == '__main__':
    run()
