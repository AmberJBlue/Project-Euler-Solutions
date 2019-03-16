
import common
def solve():
	numbers = 100
	higher = common.binomial(numbers + 9, 9) - 1
	lower = common.binomial(numbers + 10, 10) - (numbers + 1)
	plateau = numbers * 9
	result = higher + lower - plateau
	return str(result)


if __name__ == "__main__":
	print(solve())
