
# euler totient phi(n):
#  # of numbers less than n and relative prime to n

# Two distinct primes, p and q, are always relatively primes,
# (p, q) = 1, as are any positive integer powers of distinct primes
# p, q, i.e. (p^m, q^n) = 1
LIMIT = int(1e6)
# LIMIT = 11

from math import ceil, sqrt

def is_prime(x):
  return not any(
    x % y == 0
    for y in xrange(2, int(sqrt(x))+1 ))


def totient_maximum(limit):
  max_ratio = 0.0
  max_n = 0

  primes = []
  totients = [None] * (limit + 2)

  print("{:4}, {:6}, {:6}".format(
    "n", "phi(n)", "n/phi(n)"))

  for n in xrange(2, limit):
    if is_prime(n):
      primes.append(n)
      p_1, p_2 = n, n*n
      while p_2 < limit:
        totients[p_2] = p_2 - p_1
        p_1 = p_2
        p_2 *= n
      continue

    if totients[n] is not None:
      phi_n = totients[n]
    else:
      phi_n = float(n)
      for p in primes:
        if n % p == 0:
          phi_n *= (1.0 - 1.0/float(p))

    ratio = float(n)/phi_n
    # print("{:4}, {:.2}, {:.2}".format(
    #   n, phi_n, ratio))

    if n % 1000 == 0:
      print("n: {}, max_ratio: {}, some primes: {}".format(
        n, max_ratio, primes[-5:]))

    if ratio > max_ratio:
      max_ratio = ratio
      max_n = n
      print("new max_ratio: {}, {}, {}".format(
        max_n, max_ratio, primes[-5:]))
  return max_n

print(totient_maximum(LIMIT))
