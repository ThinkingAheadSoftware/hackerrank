def maximum_subarray(L):
    curr_sum = 0
    max_sum_pos = sum([x for x in L if x > 0])
    best_sum = 0

    for i, x in enumerate(L):
        val = curr_sum + x
        if val > 0:
            curr_sum = val
        else:
            curr_sum = 0

        if curr_sum > best_sum:
            best_sum = curr_sum

    max_sum = best_sum

    max_sum, max_sum_pos = (max(L), max(L)) if max_sum == 0 else (max_sum, max_sum_pos)

    return max_sum, max_sum_pos


if __name__ == '__main__':
    T = int(raw_input())
    data = []
    for T in xrange(0, T):
        N = int(raw_input())
        a = raw_input()
        data.append([int(x) for x in a.split(" ")])

    for d in data:
        print "%s %s" % maximum_subarray(d)
