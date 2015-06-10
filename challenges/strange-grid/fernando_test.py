from fernando import strange_grid

print strange_grid(6, 3)

assert(strange_grid(6, 3) == 25)

print strange_grid(1, 1)

assert(strange_grid(1, 1) == 0)

print strange_grid(500, 5)

assert(strange_grid(500, 5) == 2499)

print strange_grid(501, 5)

assert(strange_grid(501, 5) == 2508)

print strange_grid(2000000001, 3)

assert(strange_grid(2000000001, 3) == 10000000004)
