FILENAME = "./data/p082_matrix.txt"
# FILENAME = "./data/p082_matrix_test.txt"


def path_sum_three_ways(matrix):
  nx, ny = len(matrix), len(matrix[0])

  previous = [0] * ny

  for x in xrange(nx):
    # print("x: {}".format(x))
    current0 = [
      previous[y] + matrix[y][x] for y in xrange(ny)
    ]
    # print("\tcurrent0: {}".format(current0))

    current1 = [current0[0]] + [float('inf')] * (ny-1)
    for y in xrange(1, ny):
      current1[y] = min(
        current0[y],
        matrix[y][x] + current1[max(y-1, 0)]
      )

    # print("\tcurrent1: {}".format(current1))

    current2 = [float('inf')] * (ny-1) + [current0[ny-1]]
    for y in xrange(ny-2, -1, -1):
      current2[y] = min(
        current0[y],
        matrix[y][x] + current2[min(y+1, ny-1)]
      )

    if x == nx-1:
      for row in zip(current0, current1, current2):
        print("\t{}".format(row))
    previous = [min(current0[y], current1[y], current2[y]) for y in xrange(ny)]

  return previous

def main():
  with open(FILENAME, 'r') as f:
    MATRIX = [
      [int(x) for x in row.strip().split(',')]
      for row in f
    ]

  print(min(path_sum_three_ways(MATRIX)))

if __name__ == "__main__":
  main()
