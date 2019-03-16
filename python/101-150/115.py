import itertools

def solve():
	m = 50
	permutations = [1]
	for n in itertools.count(1):
		s = permutations[n - 1] + sum(permutations[ : max(n - m, 0)])
		if n >= m:
			s += 1
		permutations.append(s)
		if s > 1000000:
			return str(n)


if __name__ == "__main__":
	print(solve())
