DIVISOR = 10 ** 6

from collections import Counter
from itertools import takewhile
import sys

sys.setrecursionlimit(100000)

def p(n, m, P):
  if m > n: return p(n, n, P)
  if n < 1: return 1
  if m < 2: return 1

  total = 0
  for k in xrange(1, m+1):
    sub_prob_idx = (n-k, k)
    if sub_prob_idx not in P:
      result = p(n-k, k, P)
      P[sub_prob_idx] = result
    else:
      result = P[sub_prob_idx]
    total += result % DIVISOR

  return total

def coin_partitions(target, max_pile_size, P):
  if max_pile_size == 1: return 1
  if target < 2: return 1

  new_max_pile_size = max_pile_size-1

  total = 0

  for residual in xrange(target, -1, -max_pile_size):
    sub_prob_key = (residual, new_max_pile_size)
    if sub_prob_key not in P:
      result = coin_partitions(residual, new_max_pile_size, P)
      P[sub_prob_key] = result
      # P[residual][new_max_pile_size] = result
    else:
      result = P[sub_prob_key]
      # result = P[residual][new_max_pile_size]
    total = (total + result) % DIVISOR

  return total

  # return sum(
  #   coin_partitions(new_target, pile_sizes[:-1])
  #   for new_target in xrange(target, -1, -largest_pile_size)
  # )

def with_arrays():
  MAX = 100000
  current = [1]
  diagonal = [None,1,1]

  for n in xrange(2, MAX):
    print(n)
    previous = current[:]
    current = [1]
    for j in xrange(2, n+1):
      x = previous[j] if j > n else diagonal[n]
      current.append((current[-1] + x) % DIVISOR)
    diagonal.append(current[-1])
    print(previous, current)
    assert(len(current) == len(previous)+1)

    if n > 10: break

def with_counter():
  MAX = 100000
  P = Counter(None)
  P[0,0] = 1
  P[0,1] = 1
  P[1,1] = 1

  for n in xrange(2, MAX):
    if n % 100 == 0:
      print(n-1, P[n-1,n-1], len(P))
      # if n > 10: break

    # try:
    #   bf = coin_partitions(n-1,n-1, Counter())
    #   assert P[(n-1, n-1)] == bf
    # except AssertionError:
    #   print("n: {}, got: {}, should be: {}".format(n-1, P[(n-1,n-1)], bf))
    #   return
    # if n > 100:
    #   break

    P[(n,1)] = 1
    for j in xrange(2, n+1):
      x = P[n-j, j] if n-j >= j else P[n-j, n-j]
      P[n,j] = (P[n, j-1] + x) % DIVISOR
      # print(n, j)
      # print("P({},{}) == {}, should be {}".format(n,j,P[(n,j)], coin_partitions(n,j,Counter())))
      # try:
      #   assert(P[(n,j)] == coin_partitions(n,j,Counter()))
      # except AssertionError:
      #   print("P({},{}) == {}, should be {}".format(n,j,P[(n,j)], coin_partitions(n,j,Counter())))
      #   return

    diag = (P[n,n-1] + 1) % DIVISOR
    P[n,n] = diag
    if diag % DIVISOR == 0:
      break

    # for j in xrange(1, n):
    #   if n-j-1 == j:
    #     break
    #   del P[n-j-1, j]

  print("p({}) % {} == 0".format(n, DIVISOR))

def k_range_while(predicate):
  k = 1
  while True:
    n = int((k+1)/2) * int(((-1)**((k % 2)-1)))
    if not predicate(n):
      break
    yield n
    k+=1

def g(k):
  # pentagonal numberrs
  if k == 0: return 0

  # n = k
  result = int(k*(3*k-1)/2)
  # print("g({}): {}".format(k, result))
  return result

def with_pentagonal_numbers():
  P = [1]
  n = 1
  while P[n-1] % DIVISOR != 0:
    print(n)
    P_n = sum(
      ((-1)**(k-1) * P[n-g(k)]) % DIVISOR
      for k in k_range_while(lambda x: n-g(x) >= 0)
    ) % DIVISOR
    # print(["{} * P[{}]".format((-1)**(k-1), n-g(k)) for k in xrange(1, n+1)])
    P.append(P_n)
    # print("P: {}".format(P))
    n+=1

  print("p({}) % {} == 0".format(n-1, DIVISOR))

def main():
  return with_pentagonal_numbers()
  return with_counter()
  return with_arrays()

  # n = 2
  # result = 1
  # while result % DIVISOR != 0:
  #   total = 0
  #   for k in xrange(1, m+1):
  #     sub_prob_idx = (n-k, k)
  #     P
  #     if sub_prob_idx not in P:
  #       res = p(n-k, k, P)
  #       P[sub_prob_idx] = result
  #     else:
  #       res = P[sub_prob_idx]
  #     total += result % DIVISOR


  # P = Counter()
  # k = 1
  # result = 1
  # while result % DIVISOR != 0:
  #   x = k#5*k + 4
  #   # for i in xrange((x - len(P))+1):
  #   #   P.append(Counter())
  #   result = coin_partitions(x, x, P)
  #   print(x, result)
  #   k +=1
  # print(x)


if __name__ == "__main__":
  main()
