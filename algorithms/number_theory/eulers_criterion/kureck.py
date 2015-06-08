def eulers_criterion(a, p):
    # a**((p-1)/2) = 1 % p
    # return "YES" if a**((p-1)/2) % p == 1 else "NO"
    return "YES" if pow(a, (p-1)/2, p) in (0, 1) else "NO"

n = int(raw_input())
data = []
for n in xrange(0, n):
    values = raw_input()
    data.append([int(x) for x in values.split(" ")])

for d in data:
    print eulers_criterion(d[0], d[1])
