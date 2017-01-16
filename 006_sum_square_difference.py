N = 100


def sum_square_difference(n):
	s = 0
	for i in xrange(1, n+1):
		for j in xrange(i+1, n+1):
			s += i * j

	return s * 2

print(sum_square_difference(N))