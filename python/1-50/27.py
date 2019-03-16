import common, itertools


def solution():
	result = max(((a, b) for a in range(-999, 1000) for b in range(2, 1000)),
		key=quadratic_primes)
	return str(result[0] * result[1])


def quadratic_primes(ab):
	a, b = ab
	for i in itertools.count():
		n = i * i + i * a + b
		if not is_prime(n):
			return i


isprimeprev = common.prime_check(1000)

def is_prime(n):
	if n < 0:
		return False
	elif n < len(isprimeprev):
		return isprimeprev[n]
	else:
		return common.prime(n)


if __name__ == "__main__":
	print(solution())
