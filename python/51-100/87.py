import common


def solution():
	ceiling = 50000000
	primes = common.list_primes(common.sqrt(ceiling))
	
	sums = {0}
	for i in range(2, 5):
		newsums = set()
		for p in primes:
			q = p**i
			if q > ceiling:
				break
			for x in sums:
				if x + q <= ceiling:
					newsums.add(x + q)
		sums = newsums
	return str(len(sums))


if __name__ == "__main__":
	print(solution())
