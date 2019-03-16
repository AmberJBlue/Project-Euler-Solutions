import math, sys
if sys.version_info.major == 2:
	range = xrange


def solution():
	result = sum(i for i in range(3, 10000000) if i == factorial_digit_sum(i))
	return str(result)


def factorial_digit_sum(n):
	result = 0
	while n >= 10000:
		result += leadingZeros[n % 10000]
		n //= 10000
	return result + noLeadingZeros[n]

noLeadingZeros = [sum(math.factorial(int(c)) for c in str(i)) for i in range(10000)]
leadingZeros = [sum(math.factorial(int(c)) for c in str(i).zfill(4)) for i in range(10000)]


if __name__ == "__main__":
	print(solution())
