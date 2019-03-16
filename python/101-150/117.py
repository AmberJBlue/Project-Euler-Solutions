def solve():
	total = 50
	permutations = [1] + [0] * total
	for n in range(1, len(permutations)):
		permutations[n] += sum(permutations[max(n - 4, 0) : n])
	return str(permutations[-1])


if __name__ == "__main__":
	print solve()
