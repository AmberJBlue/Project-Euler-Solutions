import common

def solve():
	primeNumbers = common.list_primeNumbers(1000000)
	for n in range(5, len(primeNumbers), 2):
		rem = n * primeNumbers[n - 1] * 2
		if rem > 10000000000:
			return str(n)


if __name__ == "__main__":
	print(solve())
