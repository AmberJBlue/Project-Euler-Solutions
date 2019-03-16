import common, sys
if sys.version_info.major == 2:
	range = xrange


def solution():
	result = 0
	isprime = common.prime_check(999999)
	primes = common.findPrimes(999999)
	consecutive = 0
	for i in range(len(primes)):
		sum = primes[i]
		consec = 1
		for j in range(i + 1, len(primes)):
			sum += primes[j]
			consec += 1
			if sum >= len(isprime):
				break
			if isprime[sum] and consec > consecutive:
				result = sum
				consecutive = consec
	return str(result)


if __name__ == "__main__":
	print(solution())
