import common


def solution():
	DIGITS = 100
	MULTIPLIER = 100**DIGITS
	result = sum(
		sum(int(c) for c in str(common.sqrt(i * MULTIPLIER))[ : DIGITS])
		for i in range(100)
		if common.sqrt(i)**2 != i)
	return str(result)


if __name__ == "__main__":
	print(solution())
