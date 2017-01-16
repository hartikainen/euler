import operator as op


NUM_BALLS = 70
NUM_COLORS  = 7
NUM_PICKS = 20
NUM_BALLS_PER_COLOR = NUM_BALLS  / NUM_COLORS


def ncr(n, r):
  r = min(r, n-r)
  if r == 0: return 1
  numer = reduce(op.mul, xrange(n, n-r, -1))
  denom = reduce(op.mul, xrange(1, r+1))
  return numer//denom

def count_fixed_color_combinations(colors_left, picks_left=NUM_PICKS, counts=None, s=None):
  if counts is None:
    counts = []

  if s is None: s = [0]

  if colors_left == 1:
    s[0] += reduce(op.mul, (ncr(NUM_BALLS_PER_COLOR, c) for c in counts+[picks_left]))
    return s[0]

  for ball_count in xrange(
      max(1, picks_left - (colors_left-1) * NUM_BALLS_PER_COLOR),
      min(picks_left - (colors_left-1), NUM_BALLS_PER_COLOR) + 1):
    count_fixed_color_combinations(colors_left-1,
                                   picks_left - ball_count,
                                   counts + [ball_count],
                                   s)

  return s[0]

def n_color_count(n):
  count = ncr(NUM_COLORS, n) * count_fixed_color_combinations(n)
  return count

def under_the_rainbow():
  s = NUM_COLORS * (1 -
                    float(ncr(NUM_BALLS-NUM_BALLS_PER_COLOR, NUM_PICKS)) /
                    float(ncr(NUM_BALLS, NUM_PICKS)))
  return s
  s = 0
  for N in xrange(2, NUM_COLORS+1):
    s += N * (float(n_color_count(N)) / ncr(NUM_BALLS, NUM_PICKS))
  return s

  # s = 0
  # for ball_1_count in xrange(1, NUM_BALLS_PER_COLOR + 1):
  #   picks_left_1 = NUM_PICKS - ball_1_count
  #   for ball_2_count in xrange(
  #       max(1, NUM_PICKS - ball_1_count - NUM_BALLS_PER_COLOR),
  #       min(picks_left_1-1, NUM_BALLS_PER_COLOR) + 1):

  #     ball_3_count = NUM_PICKS - ball_1_count - ball_2_count
  #     s += reduce(op.mul, (ncr(NUM_BALLS_PER_COLOR, c) for c in [ball_1_count, ball_2_count, ball_3_count]))
  #     assert ball_3_count + ball_2_count + ball_1_count == NUM_PICKS
  #     assert ball_3_count > 0
  #     assert ball_1_count <= NUM_BALLS_PER_COLOR
  #     assert ball_2_count <= NUM_BALLS_PER_COLOR
  #     assert ball_3_count <= NUM_BALLS_PER_COLOR
  # s *= ncr(NUM_COLORS, 3)
  # assert all(x in ARRAY2 for x in ARRAY1)
  # print([x for x in sorted(ARRAY1)])
  # print("\n")
  # print([x for x in sorted(ARRAY2)])
  # print(s, jiiri)
  # assert s == jiiri

if __name__ == "__main__":
  print(under_the_rainbow())
