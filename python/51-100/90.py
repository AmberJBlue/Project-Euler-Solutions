import common


def solution():
	result = sum(1
		for i in range(1 << 10)
		for j in range(i, 1 << 10)  # Ensure i <= j to force the dice to be orderless
		if common.popcount(i) == common.popcount(j) == 6 and is_arrangement_valid(i, j))
	return str(result)


def is_arrangement_valid(a, b):
	if test_bit(a, 6) or test_bit(a, 9):
		a |= (1 << 6) | (1 << 9)
	if test_bit(b, 6) or test_bit(b, 9):
		b |= (1 << 6) | (1 << 9)
	return all(((test_bit(a, c) and test_bit(b, d)) or (test_bit(a, d) and test_bit(b, c)))
		for (c, d) in roots)


def test_bit(x, i):
	return ((x >> i) & 1) != 0


roots = [(i**2 // 10, i**2 % 10) for i in range(1, 10)]


if __name__ == "__main__":
	print(solution())
