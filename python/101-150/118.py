import common


def solve():
	primeCheck = common.list_primality(10000)
	digits = list(range(1, 10))
	
	def primeCounter(startindex, prev):
		if startindex == len(digits):
			return 1
		else:
			result = 0
			for split in range(startindex + 1, len(digits) + 1):
				curr = int("".join(map(str, digits[startindex : split])))
				if curr > prev and validatePrime(curr):
					result += primeCounter(split, curr)
			return result
	
	def validatePrime(n):
		if n < len(primeCheck):
			return primeCheck[n]
		else:
			return common.validatePrime(n)
	
	result = 0
	while True:
		result += primeCounter(0, 0)
		if not common.next_permutation(digits):
			break
	return str(result)


if __name__ == "__main__":
	print(solve())
