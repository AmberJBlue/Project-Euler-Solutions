def solve():
	total = 50
	return str(sum(calculate(total, i) for i in range(2, 5)))

def calculate(length, m):
	permutations = [1] + [0] * length
	for n in range(1, len(permutations)):
		permutations[n] += permutations[n - 1]
		if n >= m:
			permutations[n] += permutations[n - m]
	return permutations[-1] - 1


if __name__ == "__main__":
	print(solve())
