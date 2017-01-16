TARGET = 100

def counting_summations(target, numbers):
  if target < 0: return 0
  if len(numbers) == 1: return 1

  subproblems = [
    counting_summations(x, numbers[0:-1])
    for x in xrange(target, -1, -numbers[-1])
  ]

  return sum(subproblems)

print(counting_summations(TARGET, range(1, TARGET)))

# 2: 1+1
# =================
# 3: 1+1+1,
#    2+1
# =================
# 4: 1+1+1+1,
#    2+1+1, 2+2,
#    3+1
# =================
# 5: 1+1+1+1+1,
#    2+1+1+1, 2+2+1,
#    3+1+1, 3+2,
#    4+1
# =================
# 6: 1+1+1+1+1+1,
#    2+1+1+1+1, 2+2+1+1, 2+2+2,
#    3+1+1+1, 3+2+1,
#    4+1+1, 4+2,
#    5+1
# =================
# 7: 1+1+1+1+1+1+1,
#    2+1+1+1+1+1, 2+2+1+1+1, 2+2+2+1,
#    3+1+1+1+1, 3+2+1+1, 3+2+2, 3+3+1,
#    4+1+1+1, 4+2+1, 4+3,
#    5+1+1, 5+2,
#    6+1

# 100: 1+1...+1, ..., 99+1
