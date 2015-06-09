from fernando import strange_grid

print strange_grid(6, 3)

assert(strange_grid(6, 3) == 25)

print strange_grid(1, 1)

assert(strange_grid(1, 1) == 0)

print strange_grid(500, 5)

assert(strange_grid(500, 5) == 2498)

print strange_grid(500, 5)

assert(strange_grid(500, 5) == 2498)

print strange_grid(2000000000, 3)

assert(strange_grid(2000000000, 3) == 4999999996)
