LIMIT = int(1e8)
EXPECTED = {
  10: 39,
  25: 187,
  100: 2012,
  250: 10632,
  # LIMIT: None
}

from math import factorial, log
from itertools import combinations, product
from operator import mul
from helpers import generate_primes, is_prime
from collections import Counter
from datetime import datetime
from prime_stuff import primefactors

def s(n):
  m = 1
  while factorial(m) % n > 0:
    m+=1
  return m


def S(n):
  data = [s(i) for i in xrange(2, n+1)]
  return sum(s(i) for i in xrange(2, n+1))


# def factor_products(n, limit):
#   factors = xrange(1, n+1)

#   for l in xrange(1, len(factors)+1):
#     for x in combinations(factors, l):
#       prod = reduce(mul, x)
#       yield prod
#       if prod > limit: return


# def factorial_factor_count(n, primes=None):
#   if primes is None:
#     primes = generate_primes(n, list)
#   else:
#     primes = primes

#   # print(primes)
#   power = {}
#   for p in primes:
#     if p > n:
#       break
#     x = p
#     s = 0
#     while int(n / x) > 0:
#       s += int(n / x)
#       x *= p
#     power[p] = s
#   return reduce(mul, (x+1 for x in power.values()))


# def factorial_mod(n, m):
#   ans = 1
#   for i in xrange(1,n+1):
#     ans = ans * i % m
#   return ans % m


def d_p_n(p, n):
  upper = int(log(n, p))
  return sum(
    int(n/(p**k))
    for k in xrange(1, upper+1)
  )


def divisibility_of_factorials(limit):
  result = Counter()
  primes = generate_primes(limit, wrapper=list)
  prime_set = set(primes)

  for p in primes:
    result[p] = p

  start_time = datetime.now()
  for n in xrange(2, limit+1):
    if n%1000 == 0:
      end_time = datetime.now()
      print("n: {}, len(result): {}, duration: {}".format(n, len(result), end_time - start_time))
      start_time = datetime.now()
    if n in result: continue

    # if n in prime_set:
    #   result[n] = n
    #   continue

    factors = Counter(primefactors(n))

    if all(x < 2 for x in factors.values()):
      result[n] = max(factors.keys())
    else:
      # print(n, factors, [[int(p**power), int(p**power) in result] for p, power in factors.iteritems()])

      if len(factors) < 2:
        key = factors.keys()[0]
        power = factors[key]
        result[n] = next((i for i in xrange(key, int(n**0.5)+key+2, key) if d_p_n(key, i) >= power), n)

      else:
        result[n] = max(result[p**power] for p, power in factors.iteritems())
    # if result[n] != s(n):
    #   print("n: {}, should be: {}, got: {}, factors: {}".format(n, s(n), result[n], factors))
    #   return

  return sum(result.values())


def main():
  for i in EXPECTED:
    print("n: {}".format(i))
    start = datetime.now()
    S_i = S(i)
    dof_i = divisibility_of_factorials(i)
    end = datetime.now()
    print("time_elapsed: {}, S(n): {}, dof(n): {}".format(end-start, S_i, dof_i))

if __name__ == "__main__":
  main()
