from __future__ import division
from math import sqrt

LIMIT = int(1e6)
# LIMIT = 100
TARGET = [3, 7]


def is_prime(x):
  return not any(x%i == 0 for i in xrange(2, int(sqrt(x)) + 1))

def gcd(a, b):
  if b > a: return gcd(b, a)
  if b == 1: return 1
  if b == 0: return a
  return gcd(b, a%b)

def ordered_fractions(limit, target):
  n, d = (2, 5)
  multiplier = int((limit - d) / target[1])
  print((n + multiplier * target[0]),(d + multiplier * target[1]))
  return(multiplier)

print(ordered_fractions(LIMIT, TARGET))
