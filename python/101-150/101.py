import itertools
from fractions import Fraction

x = 10
def solve():
	solution = Fraction(0, 1)
	for k in range(1, x + 1):
		for n in itertools.count(k + 1):
			if n == x + 2:
				raise AssertionError()
			reference = Fraction(generating_function(n), 1)
			term = optimum_polynomial(k, n)
			if term != reference:
				solution += term
				break
	return str(solution.numerator) + ("" if solution.denominator == 1 else "/" + str(solution.denominator))


def optimum_polynomial(k, n):
	# Lagrange interpolation
	total = Fraction(0, 1)
	for i in range(k + 1):
		product = Fraction(generating_function(i), 1)
		for j in range(1, k + 1):
			if j != i:
				product *= Fraction(n - j, i - j)
		total += product
	return total


def generating_function(n):
	return sum((-n)**i for i in range(x + 1))


if __name__ == "__main__":
	print(solve())
