
MATRIX = []
with open("./data/p081_matrix.txt", "r") as f:
	for line in f:
		MATRIX.append([int(x) for x in line.split(",")])

def print_matrix(X):
	height, width = len(X), len(X[0])
	print(
		"\n".join(["  ".join([
			str(X[j][i]) for i in xrange(width)]
		) for j in xrange(height)])
	)

def path_sum_two_ways(matrix):
	width, height = len(matrix), len(matrix[0])
	sums = [[0 for w in xrange(width)] for y in xrange(height)]

	# initialization
	sums[0][0] = matrix[0][0]
	for h in xrange(1, height):
		sums[h][0] = matrix[h][0] + sums[h-1][0]
	for w in xrange(1, width):
		sums[0][w] = matrix[0][w] + sums[0][w-1]

	print_matrix(matrix)
	print_matrix(sums)

	for i in xrange(1, height):
		for j in xrange(1, width):
			sums[j][i] = min(sums[j-1][i], sums[j][i-1]) + matrix[j][i]

	print_matrix(sums)

	return sums[height-1][width-1]

print(path_sum_two_ways(MATRIX))