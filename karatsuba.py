import math


def karatsuba(x, y):
    '''
    Karatsuba algorithm.

    x - integer.
    y - integer.

    returns x * y

    Average complexity - O(n ** 1.59).
    '''

    if 0 in (x, y):
        return 0

    nx = math.ceil(math.log10(x))
    ny = math.ceil(math.log10(y))
    n = max(nx, ny)

    if n == 1:
        return x * y

    half_n = n // 2

    xl = x // 10 ** half_n
    xr = x % 10 ** half_n
    yl = y // 10 ** half_n
    yr = y % 10 ** half_n

    p1 = karatsuba(xl, yl)
    p2 = karatsuba(xr, yr)
    p3 = karatsuba(xl + xr, yl + yr)

    return p1 * 10 ** (2 * half_n) + (p3 - p1 - p2) * 10 ** half_n + p2
