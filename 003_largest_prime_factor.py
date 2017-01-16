target = float(600851475143)
current = target
factors = []
x = 2

from math import sqrt, ceil

def is_prime(x):
	for divider in xrange(2, (int(x**0.5)+1) + 1):
		if x % divider == 0:
			return divider, False
	return divider, True

divider, prime = is_prime(current)
while not prime:
	# x is prime
	factors.append(divider)
	current = current / divider
	print("checking primality for {}".format(current))
	divider, prime = is_prime(current)
	print(divider, prime)

factors.append(current)
print(factors)
