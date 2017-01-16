FILENAME = "./data/p011_grid.txt"
PRODUCT_LENGTH = 4

def largest_product_in_a_grid(grid, l):
  pass


def main():
  with open(FILENAME, 'r') as f:
    grid = [
      [float(x) for x in row.strip().split()]
      for row in f
    ]
  print(largest_product_in_a_grid(grid, PRODUCT_LENGTH))


if __name__ == "__main__":
  main()
