LIMIT = 1000
divisors = [3, 5]

def multiples_of_3_and_5(limit):
	multiples = []
	for i in xrange(limit):
		if (i % 3 == 0) or (i % 5 == 0):
			multiples.append(i)

	x = sum(multiples)
	return x


print(multiples_of_3_and_5(LIMIT))

def multiples_of_3_and_5_2(limit, divisors):
	first_common_divisor = None

	for i in xrange(limit, 0, -1):
		print(i, [i % d for d in divisors])
		if all((i % d) == 0 for d in divisors):
			first_common_divisor = i
			break
	print(first_common_divisor)

	s = 0
	for d in divisors:
		# sum of elements in [1, ..., first_common_divisor] divisible by d
		term_count = first_common_divisor / d
		sum_of_terms = int(term_count * float(first_common_divisor + d) / 2.0)
		s + sum_of_terms

multiples_of_3_and_5_2(LIMIT, divisors)
#1.5*(int)(($x-1)/3)*(int)(($x+2)/3) + 2.5*(int)(($x-1)/5)*(int)(($x+4)/5) - 7.5*(int)(($x-1)/15)*(int)(($x+14)/15);