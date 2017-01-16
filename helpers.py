# class Memoize:
#   def __init__(self, fn):
#     self.fn = fn
#     self.cache = {}

#   def __call__(self, arg):
#     if arg not in self.cache:
#       self.cache[arg] = self.fn(arg)
#     return self.cache[arg]

class MemoizeWithCache:
  def __init__(self, cache=None):
    self.cache = {} if cache is None else cache

  def __call__(self, fn):
    self.fn = fn
    def wrap_fn(*argc, **argv):
      if argc not in self.cache:
        self.cache[argc] = self.fn(*argc, **argv)
      return self.cache[argc]
    return wrap_fn

def memoize(cache=None):
  cache = {} if cache is None else cache
  def wrap_fn(fn):
    def wrap_wrap_fn(cachable, **argv):
      if cachable not in cache:
        result = fn(cachable, **argv)
        cache[cachable] = result
      else:
        result = cache[cachable]
      return result
    return wrap_wrap_fn
  return wrap_fn


def is_prime(x):
	for divider in xrange(2, (int(x**0.5)+1) + 1):
		if x % divider == 0:
			return divider, False
	return divider, True

def is_prime(n):
  if n == 1: return False
  if n % 2 == 0 and n > 2:
    return False
  return all(n % i for i in range(3, int(n**0.5) + 1, 2))


def generate_primes(limit, wrapper=set):
  primes = [False] * (limit+1)
  primes[0:3] = [True, False,  False]
  p = 2

  while True:
    for i in xrange(2*p, limit+1, p):
      primes[i] = True

    p = next((i for i in xrange(p+1, limit+1) if not primes[i]), None)
    if p is None: break

  if wrapper:
    return wrapper(i for i, p in enumerate(primes) if not p and i > 1)
  else:
    return (i for i, p in enumerate(primes) if not p and i > 1)
