"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = range(200)
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
cache = {}

for k in q:
    if k not in cache:
        cache[k] = f(k)

for k in q:
    for l in q:
        for i in q:
            for j in q:
                if cache[k] + cache[l] == cache[i] - cache[j]:
                    print(k, l, i, j)
