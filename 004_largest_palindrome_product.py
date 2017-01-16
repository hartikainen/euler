def largest_palindrome_product(max_digits):
	if max_digits < 1: return 0

	longest = "0"
	longest_val = 0

	for i in xrange(10**max_digits-1, 0, -1):
		for j in xrange(i, 0, -1):
			m_int = i*j
			m = str(m_int)
			print("i: {}, j: {}, m: {}".format(i, j, m))
			l = len(m)
			if m_int <= longest_val: continue

			is_palindrome = all([m[a] == m[l-a-1] for a in xrange((l/2)+1)])
			if is_palindrome:
				longest, longest_val = m, m_int
				# print("got longest: {}, {}".format(m, l))

	return longest
print(largest_palindrome_product(3))