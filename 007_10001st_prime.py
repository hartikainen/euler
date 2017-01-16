from math import sqrt

TARGET = 10001
# TARGET = 6

def is_prime(x):
	c = int(sqrt(x)) + 1
	return all(x % i != 0 for i in xrange(2, c))

def find_ordinal_prime(target):
	counter = 0
	i = 2

	while counter < target:
		if is_prime(i):
			counter += 1
		i += 1
	return(i-1)

print(find_ordinal_prime(TARGET))