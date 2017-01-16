
LIMIT = 2000000
#LIMIT = 50

import time
def summation_of_primes(limit):
	marked = set()
	primes = []
	current = 2

	while current < limit:
		for i in xrange(current*2, limit, current):
			marked.add(i)

		primes.append(current)
		current = next(
			(x for x in xrange(current+1, limit) if x not in marked),
			limit
		)

	return sum(primes)


start = time.time()
print(summation_of_primes(LIMIT))
end = time.time()
print("duration: {}".format(end-start))
