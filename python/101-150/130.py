
import common, itertools, sys
if sys.version_info.major == 2:
	filter = itertools.ifilter


def solve():
	cond = lambda i: (i % 5 != 0) and (not common.is_prime(i)) \
		and ((i - 1) % leastDivisible(i) == 0)
	result = sum(itertools.islice(filter(cond, itertools.count(7, 2)), 25))
	return str(result)


def leastDivisible(n):
	if n % 2 == 0 or n % 5 == 0:
		return 0
	sum = 1
	pow = 1
	k = 1
	while sum % n != 0:
		k += 1
		pow = pow * 10 % n
		sum = (sum + pow) % n
	return k


if __name__ == "__main__":
	print(solve())
