import math


def solution():
	ceiling = 10**6
	result = sum(1 for i in range(ceiling) if get_chain_length(i) == 60)
	return str(result)


def get_chain_length(n):
	seen = set()
	while True:
		seen.add(n)
		n = factorialize(n)
		if n in seen:
			return len(seen)


def factorialize(n):
	result = 0
	while n != 0:
		result += FACTORIAL[n % 10]
		n //= 10
	return result

FACTORIAL = [math.factorial(i) for i in range(10)]


if __name__ == "__main__":
	print(solution())
