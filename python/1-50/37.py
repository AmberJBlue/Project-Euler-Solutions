import common, itertools, sys
if sys.version_info.major == 2:
	filter = itertools.ifilter


def solution():
	result = sum(itertools.islice(filter(truncated_prime_check, itertools.count(10)), 11))
	return str(result)


def truncated_prime_check(n):
	i = 10
	while i <= n:
		if not common.prime(n % i):
			return False
		i *= 10
	
	while n > 0:
		if not common.prime(n):
			return False
		n //= 10
	return True


if __name__ == "__main__":
	print(solution())
