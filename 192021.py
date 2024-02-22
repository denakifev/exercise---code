from functools import lru_cache
def moves(h1, h2):
    return (h1 , h2 + 1), (h1+1, h2), (h1+h2, h2), (h1, h2+h1)
@lru_cache(None)
def f(h1, h2):
    if h1 + h2 >= 75:
        return 'end'
    if (any(f(*m) == 'end' for m in moves(h1, h2))):
        return 'P1'
    if (all(f(*m) == 'P1' for m in moves(h1, h2))):
        return 'v1'
    if (any(f(*m) == 'v1' for m in moves(h1, h2))):
        return 'p2'
    if (all(f(*m) == 'p2' or f(*m) == 'P1' for m in moves(h1, h2))):
        return 'v2'


for i in range(1, 67):
    print(f(i, 7), i)
