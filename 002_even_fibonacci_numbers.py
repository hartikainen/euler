LIMIT = 4e6
data = [None, 1,2]
even_sum = 2

import time

start = time.time()

while True:
	print(data)
	data[0:2] = data[1:3]
	new_fibonacci = sum(data[0:2])
	if new_fibonacci > LIMIT: break

	data[2] = new_fibonacci

	if new_fibonacci % 2 == 0:
		print("new fibonacci: {}".format(new_fibonacci))
		even_sum += new_fibonacci

print(even_sum)
end = time.time()
print("time elapsed: {}".format(end - start))

def even_fibonacci_numbers(limit):
	x = y = 1
	s = 0
	while s < limit:
		s += (x + y)
		x, y = (x + 2*y), (2*x + 3*y)
	return s

start = time.time()
print(even_fibonacci_numbers(LIMIT))
end = time.time()
print("time elapsed: {}".format(end - start))
