import fractions

def solution():
	numerator = 1
	denomenator = 1
	for d in range(10, 100):
		for n in range(10, d):
			n0 = n % 10
			n1 = n // 10
			d0 = d % 10
			d1 = d // 10
			if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
				numerator *= n
				denomenator *= d
	return str(denomenator // fractions.gcd(numerator, denomenator))


if __name__ == "__main__":
	print(solution())
