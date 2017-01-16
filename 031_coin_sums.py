COINS = [1,2,5,10,20,50,100,200]
TARGET = 200

def coin_sums(coins, target):
	print(
		"called coins_sums with coins {} and target {}".format(coins, target)
	)
	if len(coins) == 1: return 1
	subproblems = [
		coin_sums(coins[0:-1], x)
		for x in xrange(target, -1, -coins[-1])
	]
	return sum(subproblems)

print(coin_sums(COINS, TARGET))
