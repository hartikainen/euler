def amazing_mazes(m, n):
  data = [[[0,0,0,0] for x in xrange(n)] for y in xrange(m)]

  for x in xrange(0, n):
    pass


print(amazing_mazes(2, 3))

def jiiri(x_0, y_0, column):
  x, y = x_0, y_0

  for i in xrange(2, column+1):
    x, y = 2*x + 2*y, x + y
  return x, y

print jiiri(2, 3, 3)
