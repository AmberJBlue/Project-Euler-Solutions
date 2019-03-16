import common, itertools, sys
if sys.version_info.major == 2:
	filter = itertools.ifilter


def solution():
	cond = lambda n: num_prime_sum_ways(n) > 5000
	result = next(filter(cond, itertools.count(2)))
	return str(result)


primes = [2]

def num_prime_sum_ways(n):
	for i in range(primes[-1] + 1, n + 1):
		if common.is_prime(i):
			primes.append(i)
	
	ways = [1] + [0] * n
	for p in primes:
		for i in range(n + 1 - p):
			ways[i + p] += ways[i]
	return ways[n]


if __name__ == "__main__":
	print(solution())
