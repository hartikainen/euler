FILE_PATH = "./data/p099_base_exp.txt"
from math import log

def largest_exponential(filepath):
	largest = [1, 1] # base, exp
	with open(filepath) as f:
		for i, line in enumerate(f):
			base, exp = map(int, line.split(","))
			if exp * log(base, 2) > largest[1] * log(largest[0], 2):
				largest = [base, exp]
				largest_i = i + 1

	return largest_i

print(largest_exponential(FILE_PATH))