from kureck import maximum_subarray

L1 = [2, -1, 2, 3, 4, -5]

print maximum_subarray(L1)

assert(maximum_subarray(L1) == (10, 11))

L2 = [-1, -2, -3, -4, -5, -6]

print maximum_subarray(L2)

assert(maximum_subarray(L2) == (-1, -1))

L3 = [1, -1, -1, -1, -1, 5]

print maximum_subarray(L3)

assert(maximum_subarray(L3) == (5, 6))
