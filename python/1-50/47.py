import common, itertools, sys
if sys.version_info.major == 2:
	filter = itertools.ifilter


def solution():
	cond = lambda i: all((count_distinct_prime_factors(i + j) == 4) for j in range(4))
	result = next(filter(cond, itertools.count()))
	return str(result)


@common.memoize
def count_distinct_prime_factors(n):
	count = 0
	while n > 1:
		count += 1
		for i in range(2, common.root(n) + 1):
			if n % i == 0:
				while True:
					n //= i
					if n % i != 0:
						break
				break
		else:
			break  # n is prime
	return count


if __name__ == "__main__":
	print(solution())
