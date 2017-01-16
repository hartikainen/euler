from helpers import MemoizeWithCache
from collections import Counter
from helpers import is_prime

LIMIT = 5000
EXPECTED = Counter({2:1, 3: 1, 4: 1, 5:2, 6:2, 7:3, 8: 3, 10: 5})

@MemoizeWithCache(cache=Counter())
def p(n, primes):
  if n < 0: return 0
  if n == 0: return 1
  if len(primes) == 1: return int(n%primes[0] == 0)

  first_primes, highest_prime = tuple(primes[:-1]), primes[-1]
  return sum(
    p(x, first_primes) for x in xrange(n, -1, -highest_prime)
  )


def main():
  n = 2
  primes = [2]

  while p(n, tuple(primes)) <= LIMIT:
    print(n)
    if n in EXPECTED:
      if p(n, tuple(primes)) != EXPECTED[n]:
        print("p({}) == {}, should be: {}".format(n, p(n, tuple(primes)), EXPECTED[n]))
      assert(p(n, tuple(primes)) == EXPECTED[n])
    n+=1
    if is_prime(n):
      primes.append(n)

  print("p({}) == {} > {}".format(n, p(n, tuple(primes)), LIMIT))


if __name__ == "__main__":
  main()
