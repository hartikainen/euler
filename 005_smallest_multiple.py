DIVISORS = range(1, 21)

def smallest_multiple(divisors):
	max_divisor = max(divisors)
	i = max_divisor
	while(True):
		if all([i % j == 0 for j in divisors]):
			break
		i += max_divisor

	return i

print(smallest_multiple(DIVISORS))