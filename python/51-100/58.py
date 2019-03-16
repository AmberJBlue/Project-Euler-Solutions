import common, fractions, itertools

def solution():
	TARGET = fractions.Fraction(1, 10)
	numprimes = 0
	for n in itertools.count(1, 2):
		for i in range(4):
			if common.is_prime(n * n - i * (n - 1)):
				numprimes += 1
		if n > 1 and fractions.Fraction(numprimes, n * 2 - 1) < TARGET:
			return str(n)


if __name__ == "__main__":
	print(solution())
