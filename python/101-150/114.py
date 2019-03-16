def solve():
	total = 50
	permutations = [0] * (total + 1)
	for n in range(len(permutations)):
		if n < 3:
			permutations[n] = 1
		else:
			permutations[n] = permutations[n - 1] + sum(permutations[ : n - 3]) + 1
	return str(permutations[-1])


if __name__ == "__main__":
	print(solve())
