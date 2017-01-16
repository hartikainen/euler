
from collections import defaultdict
import sys

sys.setrecursionlimit(100000)

def ackermann(m, n, A=None):
  # print("calling ackermann with A: {}, m: {}, n: {}".format(A, m, n))
  if A is None:
    # A = [[None for _ in xrange(n+1)] for _ in xrange(m+1)]
    A = {}# defaultdict(lambda: defaultdict(int))


  # if m not in A: A[m] = {}
  try:
    return A[m][n]
  except KeyError:
    A[m] = {}

  if m == 0:
    A[m][n] = n+1
  elif n == 0:
    A[m][n] = ackermann(m-1, 1, A)
  else:
    n2 = ackermann(m, n-1, A)
    A[m][n] = ackermann(m-1, n2, A)

  # for i in xrange(n+1):
  #   A[0][i] = i+1

  # print(A)

  # for j in xrange(m+1):
  #   for i in xrange(n+1):
  #     if j == 0:
  #       A[j][i] = i+1
  #     elif i == 0:
  #       A[j][i] = A[j-1][0]
  #     else:
  #       A[j][i] = A[j-1][A[j][i-1]]

  return A[m][n]



  # if m == 0: return n+1
  # if n == 0: return ackermann(m-1, 1)
  # return ackermann(m-1, ackermann(m, n-1))

def main():
  assert ackermann(1,0) == 2
  assert ackermann(2,2) == 7
  assert ackermann(3,4) == 125

  s = sum(ackermann(n, n) for n in xrange(7))
  print(s)
  print(s % 14**8)
  return


if __name__ == "__main__":
  main()
