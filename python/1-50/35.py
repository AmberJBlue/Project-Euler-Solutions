import common, sys
if sys.version_info.major == 2:
	range = xrange


def solution():
	isprime = common.prime_check(999999)
	def circular_prime(n):
		s = str(n)
		return all(isprime[int(s[i : ] + s[ : i])] for i in range(len(s)))
	
	result = sum(1
		for i in range(len(isprime))
		if circular_prime(i))
	return str(result)


if __name__ == "__main__":
	print(solution())
