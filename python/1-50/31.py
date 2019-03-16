def solution():
	amount = 200
	
	permutations = [1] + [0] * amount
	for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
		for i in range(len(permutations) - coin):
			permutations[i + coin] += permutations[i]
	return str(permutations[-1])


if __name__ == "__main__":
	print(solution())
