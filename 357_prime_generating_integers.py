from __future__ import division
LIMIT = int(1e8)
LIMIT = 100000000
# LIMIT = 50

from math import ceil, sqrt
from helpers import generate_primes

def is_prime(x):
  return not any(
    x % i == 0 for i in xrange(2, int(sqrt(x)) + 1)
  )

def prime_generating_integers(limit):
  count = 0
  primes = [
    x for x in xrange(2, int(sqrt(limit)) + 1)
    if is_prime(x)
  ]

  for i in xrange(1, limit+2):
    if i % 10000 == 0:
      # print("i:{}, divisors:{}".format(i, divisors))
      print("i:{}".format(i))
    # if i <= limit and i not in primes: continue
    # if not is_prime(i): continue
    if i % 2 == 0: continue
    n = i-1

    all_primes = True

    divisors = []
    for d in xrange(1, int(sqrt(n))+2):
      if n%d > 0: continue
      divisors.append(d)
      if (n/d + d) not in primes:
      # if not is_prime(n/d + d):
      #   # print("not prime: {0}/{1} + {1} = {2}".format(n, d, n/d + d))
        all_primes = False
        break

    # print("{}: {}, {}".format(n, divisors, [int(n/d + d) for d in divisors]))
    if all_primes:
      # print("all primes: {}".format(n))
      count += 1

  return count


def divisors(n):
  return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def generate_square_free_table(limit):
  sieve = {}
  # TODO


def prime_generating_integers2(limit):
  prime_table = generate_primes(limit)

  prime_generators = []
  for p, val in enumerate(prime_table):
    if p % 100000 == 0:
      print("p: {}".format(p))
    if val or p < 2: continue
    n = p-1
    if any((prime_table[(d + int(n/d))] for d in divisors(n))):
      continue
    prime_generators.append(n)

  print(prime_generators)
  return sum(prime_generators)


def prime_generating_integers3(limit):
  prime_table = generate_primes(limit)
  squarefree_table = generate_square_free_numbers(limit)

  prime_generators = []

  one_sum = 1
  for n in xrange(2, limit):
    if prime_table[n+1] or prime_table[int(n/2) + 2] or not squarefree_table[n]:
      continue

    if any((prime_table[d + int(n/d)] for d in divisors(n))):
      continue

    prime_generators.append(n)

  return sum(prime_generators)
print(prime_generating_integers2(LIMIT))
