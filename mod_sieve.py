import math
from itertools import islice, count

"""
 is it possible to transform the equilateral triangle keeping two sides fixed and alter the third side such that it
 still remains a triangle, but the altered side will have its length as an even integer, and the line drawn
 from the opposite vertex to the mid-point of the altered side is of integral length.
"""


def angle(a, b, c):
    return math.degrees(math.acos((a**2 + b**2 - c**2) / (2.0 * a * b)))


def get_bisector_length(hyp, base):
    return math.sqrt(hyp**2 - base**2)


def odd_factors(n):
    odd = set()
    limit = int(math.ceil(math.sqrt(n)))
    for i in xrange(1, limit + 1):
        if i & 1 and n % i == 0:
            odd.add(i)
        if (n / i) & 1 and n % (n / i) == 0:
            odd.add(n / i)

    return iter(odd)


def isPrime(n):
    if n < 2:
        return False
    return all(n % i for i in islice(count(2), int(math.sqrt(n) - 1)))


def seq_sieve(n):
    F = [0] * (n + 1)
    i = 2

    while i * i <= n:
        if F[i] == 0:
            k = i * i

        while k <= n:
            if F[k] == 0:
                F[k] = i

            k += i
        i += 1

    return F


def get_4k_plus_3_count(x, F):
    even_1 = 0
    even_3 = 0

    if x <= 1:
        return 0, 0
    while F[x] > 0:
        if F[x] != 2:
            if F[x] % 4 == 1:
                even_1 += 1
            if F[x] % 4 == 3:
                even_3 += 1
        x /= F[x]

    if x % 4 == 1:
        even_1 += 1
    if x % 4 == 3:
        even_3 += 1
    return even_1 * 2, even_3 * 2


def main(prime_precomp):
    for _ in xrange(input()):
        N = input()
        e1, e3 = get_4k_plus_3_count(N, prime_precomp)

        if e3 % 2 == 0:
            ans = e1
        else:
            ans = 0

        if ans != 0:
            print "YES"
        else:
            print "NO"

if __name__ == '__main__':

    prime_precomp = seq_sieve(5 * 10**6 + 10)
    main(prime_precomp)
