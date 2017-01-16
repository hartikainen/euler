from __future__ import division

LIMIT = int(1e14)


def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def is_harshad(n):
  return n % digit_sum(n) == 0

def right_truncatable_harshad_number(n):
  if not is_harshad(n): return False
  str_n = str(n)
  len_n = len(str_n)
  for i in xrange(1, len_n+1):
    truncated = int(str_n[:i])
    if not is_harshad(truncated): return False
  return True

def is_strong_harshad(n):
  return is_harshad(n) and is_prime(n/digit_sum(n))

def is_strong_right_truncatable_harshad_prime(n):
  str_n = str(n)
  len_n = len(str_n)
  prev_n = int(str_n[:len_n-1])
  return (is_prime(n) and
          is_strong_harshad(prev_n) and
          right_truncatable_harshad_number(prev_n))

def bf_harshad(limit):
  total = 0
  strong_right_truncatable = set()
  for n in xrange(10,limit):
    if is_strong_right_truncatable_harshad_prime(n):# is_prime(n) and is_strong_right_truncatable(prev_n):
      total+=n
      strong_right_truncatable.add(n)
  print(sorted(list(strong_right_truncatable)))
  print("total : {}".format(total))

def harshad_numbers(limit):
  right_truncatable = set()
  strong_right_truncatable = set()

  total = 0
  n = 1
  while n < limit:
    str_n = str(n)
    len_n = len(str_n)

    digit_pos = next((len_n-len_left
                     for len_left in xrange(1, len(str_n))
                     if int(str_n[:len_left]) not in right_truncatable),
                     None)

    # digit_pos = None
    # for len_left in xrange(1, len(str_n)):
    #   if int(str_n[:len_left]) not in right_truncatable:
    #     digit_pos = len_n-len_left
    #     break

    print("n: {}, digit_pos: {}".format(n, digit_pos))
    if n < 20:
      print("\tright_truncatable: {}".format(right_truncatable))

    if n > 9020:
      print("{}".format(list((int(str_n[:len_left])
                              for len_left in xrange(1, len(str_n))))))

    if digit_pos is not None:
      p = 10**digit_pos
      n = ((n+p) // p) * p
      continue

    digit_sum = sum(int(x) for x in str_n)
    if n % digit_sum == 0:
      right_truncatable.add(n)

      if is_prime(n/digit_sum):
        total += n
        strong_right_truncatable.add(n)

    n+=1

  return total


if __name__ == "__main__":
  # print(
  #   [x for x in xrange(1, 100) if is_prime(x)]
  # )
  # x = harshad_numbers(10000)
  x = bf_harshad(10000)
  print(x)
  # x2 = bf_harshad(10000)
  # print(x2)
  # assert x == 90619
  # print(harshad_numbers(LIMIT))
