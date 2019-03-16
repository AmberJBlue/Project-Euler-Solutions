import math

def solve():
	chances = 15
	permutations = [[1]]
	for i in range(1, chances + 1):
		row = []
		for j in range(i + 1):
			temp = 0
			if j < i:
				temp = permutations[i - 1][j] * i
			if j > 0:
				temp += permutations[i - 1][j - 1]
			row.append(temp)
		permutations.append(row)
	
	numerator = sum(permutations[chances][i] for i in range(chances // 2 + 1, chances + 1))
	denominator = math.factorial(chances + 1)
	return str(denominator // numerator)


if __name__ == "__main__":
	print(solve())
